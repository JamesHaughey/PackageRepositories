# Import builtin modules
import sys
import json
import subprocess

# Import third party packages

# Import local modules

def load_package_spec(path: str) -> dict:
    with open(path) as json_file:
        package_spec = json.load(json_file)
    return package_spec

def download_packages(package_spec: dict):
    for platform in package_spec["platforms"]:
        for version in package_spec["python_versions"]:
            for package in package_spec["packages"]:
                print(f"Platform: {platform}, Version: {version}, Package: {package}")
                cmd = [
                    sys.executable,
                    "-m", "pip",
                    "download",
                    "--implementation", "cp",
                    "--platform", platform,
                    "--python-version", version,
                    "--only-binary=:all:",
                    package
                ]
                print(cmd)
                response = subprocess.run(cmd, cwd="landing_zone/")

                if response.returncode != 0:
                    cmd = [
                        sys.executable,
                        "-m", "pip",
                        "download",
                        package
                    ]
                    response = subprocess.run(cmd, cwd="landing_zone/")
                    
                    if response.returncode != 0:
                        print("###### Package really not found #####")
                        ## TODO Insert some logging here


if __name__ == "__main__":
    package_spec = load_package_spec("download_packages/package_spec.json")
    download_packages(package_spec)