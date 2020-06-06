require 'minitest/autorun'

class TestEvacuation < Minitest::Test
  def initialize
    @evacuation = Evacuation.new
    @base_input =
      2
      3
      3 3 3
      2
      4 5
    eos
  end
end