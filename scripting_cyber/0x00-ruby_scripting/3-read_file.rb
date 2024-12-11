require 'json'

def count_user_ids(path)
    file_content = File.read(path)
    data = JSON.parse(file_content)

    user_id_counts = Hash.new(0)

    data.each do |entry|
        user_id = entry['userId']
        user_id_counts[user_id] += 1
    end

    user_id_counts.sort.each do |user_id, count|
        puts "#{user_id}: #{count}"
    end

end                                          