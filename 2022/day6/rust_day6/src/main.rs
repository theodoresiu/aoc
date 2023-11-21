use std::fs::{File,read_to_string};
use std::io::{self, BufReader, BufRead};
use std::collections::{HashSet, VecDeque};


fn main() {
    let file_path = "../input.txt";
    let data = read_to_string(file_path).unwrap();
    let starting_chars: Vec<char> = data[0..4].chars().collect();
    let mut curr_chars: VecDeque<char> = VecDeque::from(starting_chars);

    // Switch to 14 for part 2
    for (i, c) in data[4..].chars().enumerate(){
        let curr_chars_set:HashSet<char> = curr_chars.clone().into_iter().collect();
        
        if curr_chars_set.len()==4{
            println!("{}",i+4);
            break;
        }
        else{
            curr_chars.pop_front();
            curr_chars.push_back(c);
        }
    }


}
