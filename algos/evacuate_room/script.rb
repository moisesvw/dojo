def sort_members(dic)
  dic.sort_by {|a, b| -a}
end

def print_participation(members)
  mm = members.map{|k, v| k}
  total = mm.inject(0, :+).to_f
  
  puts "#{members}"
  puts "#{mm.map{|x| x/total}}"
end

cases = ARGF.readline.to_i
party_labels = ("A".."Z").to_a
idx = 0
(1..cases).each do |example|
  parties = ARGF.readline.to_i
  all_members = 0.0

  sequence = ""

  members = ARGF.readline.split(' ').each_with_index.map do |m, i|
    [m.to_i.tap {|m_| all_members += m_ }, i]
  end

  all_parties = members.count

  while !members.empty?    
    members = sort_members(members)
    # print_participation(members)

    if members.last && members.last.first == 0
      all_parties = all_parties - 1
      members.delete_at(members.count - 1) and next
    end

    members[0][0] = members[0][0] - 1
    sequence += party_labels[members[0].last]

    if members[1]
      members[1][0] =  members[1][0] - 1
      all_members -= 1
    end

    if members[1]
      sequence += party_labels[members[1].last]
      all_members -= 1
    end


    if all_parties == 3 && all_members == 3
      members[0][0] = members[0][0] - 1
      sequence = "#{sequence} #{party_labels[members[0].last]} "
      next
    else
      sequence += " "
    end

    if members.last && members.last.first == 0
      all_parties = all_parties - 1
      members.delete_at(members.count - 1)
    end

    if members.last && members.last.first == 0
      all_parties = all_parties - 1
      members.delete_at(members.count - 1)
    end
  end

  puts "Case ##{example}: #{sequence}".strip
  # puts "numbers of parties #{parties}"
  # puts "numbers of members #{members}, total: #{all_members}"
end
