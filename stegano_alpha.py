import cv2
import numpy as np
import hashlib

def hash_pin(pin):
    return hashlib.sha256(pin.encode()).hexdigest()

def embed_message(image_path, message, pin):
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    if image is None:
        raise ValueError("Gambar tidak valid")

    if image.shape[2] == 3:
        # Tambahkan channel alpha jika belum ada
        b, g, r = cv2.split(image)
        a = np.ones_like(b) * 255
        image = cv2.merge((b, g, r, a))

    h, w, _ = image.shape
    max_bytes = h * w
    full_message = hash_pin(pin) + "|" + message + chr(0)
    bits = ''.join([format(ord(c), '08b') for c in full_message])

    if len(bits) > max_bytes:
        raise ValueError("Pesan terlalu panjang untuk gambar ini.")

    alpha_channel = image[:, :, 3].flatten()
    for i in range(len(bits)):
        alpha_channel[i] = np.uint8((int(alpha_channel[i]) & ~1) | int(bits[i]))
    image[:, :, 3] = alpha_channel.reshape((h, w))

    return image

def extract_message(image_path, pin):
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    if image is None or image.shape[2] != 4:
        return "", False

    h, w, _ = image.shape
    alpha_channel = image[:, :, 3].flatten()
    bits = ''.join([str(alpha_channel[i] & 1) for i in range(len(alpha_channel))])
    bytes_list = [bits[i:i+8] for i in range(0, len(bits), 8)]
    chars = [chr(int(b, 2)) for b in bytes_list if len(b) == 8]

    message = ''
    for ch in chars:
        if ch == '\x00':
            break
        message += ch

    if '|' in message:
        received_hash, extracted_msg = message.split('|', 1)
        expected_hash = hash_pin(pin)
        if received_hash == expected_hash:
            return extracted_msg, True
    return "", False
