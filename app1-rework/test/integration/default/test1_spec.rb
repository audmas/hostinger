require 'serverspec'

set :backend, :exec

describe command('cat hir1.txt') do
  its(:stdout) { should match /sw/ }
end

describe command('net show bgp neighbor 192.168.15.79') do
  its(:stdout) { should match /BGP state = Established/}
end