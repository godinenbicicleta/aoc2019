defmodule Day4 do

  def count_passwords(start_num, end_num) do
    Enum.filter(
      start_num..end_num,
      &check_rules/1
    )
    |> Enum.count
  end

  def check_rules(password) do
    cond1 = check_adjacent(password)
    cond2 = check_nondecreasing(password)
    case {cond1, cond2} do
      {true, true} -> true
      _ -> false
    end
  end

  def check_adjacent(num) do
    digits = Integer.to_string(num)
             |> String.codepoints

    min_adjacent = Enum.reduce(digits, %{}, fn 
      digit, dic ->
        Map.update(dic,digit,1, fn x -> x+1 end)
    end)
    |> Enum.filter(fn {_d,val} -> val > 1 end)
    |> Enum.count
     
    min_adjacent > 0 
  end

  def check_nondecreasing(num) do
    digits = Integer.to_string(num)
             |> String.codepoints
             |> Enum.map(&String.to_integer/1)

    Enum.sort(digits) == digits
  end

end
