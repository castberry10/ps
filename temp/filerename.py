import os

def remove_trailing_spaces_in_filenames(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        # 먼저 디렉토리 이름의 후행 공백을 제거
        for dirname in dirnames:
            new_dirname = dirname.rstrip()
            if dirname != new_dirname:
                old_path = os.path.join(dirpath, dirname)
                new_path = os.path.join(dirpath, new_dirname)
                print(f'Renaming directory: "{old_path}" -> "{new_path}"')
                os.rename(old_path, new_path)

        # 파일 이름의 후행 공백을 제거
        for filename in filenames:
            new_filename = filename.rstrip()
            if filename != new_filename:
                old_path = os.path.join(dirpath, filename)
                new_path = os.path.join(dirpath, new_filename)
                print(f'Renaming file: "{old_path}" -> "{new_path}"')
                os.rename(old_path, new_path)

# 사용법: root_dir에 처리할 최상위 디렉토리 경로를 지정
root_dir = "./"
remove_trailing_spaces_in_filenames(root_dir)
