require 'json'
def merge_json_files(file1_path, file2_path)
    file_data = File.read(file1_path)
    json_data = JSON.parse(file_data)

    File.write(file2_path, JSON.dump(json_data))
end