use std::collections::{VecDeque, HashSet};
use std::fs::File;
use std::io::{self, BufReader, BufRead};


fn process_directory(lines: &mut VecDeque<String>, result: &mut HashSet<i32>)->i32 {
    let mut curr_sum = 0;
    while lines.len()>0{
        let line =  lines.pop_front().unwrap();
        let cmd_args: Vec<&str> = line.split(" ").collect();
        let n1: &str = cmd_args[0];
        let n2: &str = cmd_args[1];
        if n1.as_bytes()[0].is_ascii_digit(){
            let val: i32 = n1.parse().unwrap();
            curr_sum = curr_sum + val;
        }

        if n2 == "cd"{
            let n3:&str = cmd_args[2];
            if n3 == ".."{
                if curr_sum < 100000{
                let elem = result.iter().next().unwrap().clone();
                result.remove(&elem);
                result.insert(elem+curr_sum);
                return curr_sum
                }
            }
            else{
                curr_sum = curr_sum + process_directory(lines, result);
            }
        }
      }
      if curr_sum < 100000{
        let elem = result.iter().next().unwrap().clone();
        result.remove(&elem);
        result.insert(elem+curr_sum);
        return curr_sum
    }
    return curr_sum

}

fn main() {
    let file_path = "../input.txt";
    let file = File::open(file_path).unwrap();

    let reader = BufReader::new(file);
    let lines: Vec<String> = reader.lines().map(|l| l.unwrap()).collect();
    let mut lines: VecDeque<String> = lines.into_iter().collect();
    let mut result: HashSet<i32> = HashSet::from([0]);
    process_directory(&mut lines, &mut result);
    println!("{:?}",result);

}
