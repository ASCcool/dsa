def toh(disk, src, dest, aux):
    if disk == 0:
        return
    toh(disk-1, src, aux, dest)
    print(f"Moved disk {disk} from {src} to {dest}")
    toh(disk-1, aux, dest, src)


if __name__ == "__main__":
    toh(3, "A", "C", "B")
