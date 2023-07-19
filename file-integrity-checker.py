import hashlib
from rich.console  import Console


console = Console()

def get_file_hash(filename):

  with open(filename, "rb") as f:
    data = f.read()


  return hashlib.sha256(data).hexdigest()


def check_file_integrity(filename, expected_hash):


  actual_hash = get_file_hash(filename)


  if actual_hash == expected_hash:
    return True

  else:
    console.print("""File integrity check failed.""",style="bold red on white")
    console.print("""[>] Expected hash: {}, actual hash: {}""".format(expected_hash, actual_hash), style="bold red")

    return False

if __name__ == "__main__":

  filename = "example.txt"
  expected_hash = "<hash>"

  if check_file_integrity(filename, expected_hash):
    console.print("[*] File integrity check passed.", style="bold green")
