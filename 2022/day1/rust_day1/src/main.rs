use std::fs::File;
use std::process::Command;
use std::io::{self, BufReader, BufRead};
use std::collections::BinaryHeap;

fn main() {
    let file_path = "../input.txt";
    let file = File::open(file_path).unwrap();

    let reader = BufReader::new(file);

    let mut curr_sum = 0;
    let mut max_sum = 0;
    let mut h = BinaryHeap::new();
    for line in reader.lines() {
        let line_string = line.unwrap();
        if line_string.is_empty(){
            if max_sum < curr_sum{
                max_sum = curr_sum;
            }
            h.push(curr_sum);
            curr_sum =0
        }
        else{
            let line_num: i32 = line_string.parse().unwrap();
            curr_sum = curr_sum + line_num;
        }
    }
    let mut max_three = 0;
    for _ in 0..3 { 

        let max_num = h.pop().unwrap();
        max_three = max_three + max_num;

     }
    println!("Here is the single total {}",max_sum);
    println!("Here is my max three {}", max_three);
    

}
