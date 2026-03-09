def convert_to_binary(data):

    binary_list = []

    for item in data:
        byte_size = item["packet_size_bytes"]

        binary_value = format(byte_size, '08b')

        binary_list.append({
            "bytes": byte_size,
            "bits": item["packet_size_bits"],
            "binary": binary_value
        })

    return binary_list