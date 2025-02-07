from dotenv import load_dotenv, find_dotenv


env_file_path = find_dotenv(usecwd=True, raise_error_if_not_found=False)
if env_file_path:
    load_dotenv(env_file_path, override=True)


print_error = lambda msg: print(f'\033[91m{msg}\033[0m')
print_warning = lambda msg: print(f'\033[93m{msg}\033[0m')
