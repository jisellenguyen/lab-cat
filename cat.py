'''
This program prints stdin to the screen.
'''
import sys

def cat(file):
    # Read in chunks to keep memory usage O(1)
    chunk_size = 8192
    while True:
        chunk = file.read(chunk_size)
        if not chunk:
            break
        sys.stdout.buffer.write(chunk)
    sys.stdout.buffer.flush()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "rb") as f:
                cat(f)
    else:
        cat(sys.stdin.buffer)
