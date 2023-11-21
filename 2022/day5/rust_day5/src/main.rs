use std::fs::File;
use std::io::{self, BufReader, BufRead};
use std::collections::HashMap;



pub fn update_crates(crates: &mut HashMap<i32, Vec<&str>>,
                     to: i32, from:i32, moves: usize){
    println!("Move {} from {} to {}", moves, from, to);
    let mut to_crates = crates.get(&to).unwrap().clone();
    let from_crates = crates.get(&from).unwrap().clone();

    println!("Before");
    println!("{:?}", from_crates);
    println!("{:?}", to_crates);
    // Remove the rev for the other result
    let chop_off = from_crates.len()-moves;
    let mut to_move: Vec<&str> = from_crates.iter().skip(chop_off).rev().copied().collect();
    to_crates.append(&mut to_move);
    let from_crates: Vec<&str> = from_crates[..chop_off].to_vec();
    println!("After");
    println!("{:?}", from_crates);
    println!("{:?}", to_crates);

    crates.insert(to, to_crates);
    crates.insert(from, from_crates);

}


fn main() {
    let mut crates = HashMap::from([
        (1, vec!("D", "M", "S", "Z", "R", "F", "W", "N")),
        (2, vec!("W", "P", "Q", "G", "S")),
        (3, vec!("W", "R", "V", "Q", "F", "N", "J", "C")),
        (4, vec!("F", "Z", "P", "C", "G", "D", "L")),
        (5, vec!("T", "P", "S")),
        (6, vec!("H", "D", "F", "W", "R", "L")),
        (7, vec!("Z", "N", "D", "C")),
        (8, vec!("W", "N", "R", "F", "V", "S", "J", "Q")),
        (9, vec!("R", "M", "S", "G", "Z", "W", "V"))]);


    let file_path = "../input.txt";
    let file = File::open(file_path).unwrap();

    let reader = BufReader::new(file);
    let mut curr_score1 = "".to_string();

    for line in reader.lines() {
        let line_string = line.unwrap();
        if line_string.starts_with("move"){
            let moves: Vec<&str> = line_string.split(" ").collect();
            let num_moves:usize=moves[1].parse().unwrap();
            let from:i32 = moves[3].parse().unwrap();
            let to:i32  = moves[5].parse().unwrap();
            update_crates(&mut crates, to, from, num_moves);
        }
    }
    for i in 1..10{
        curr_score1.push_str(crates.get(&i).unwrap().last().unwrap());
    }
    println!("{}", curr_score1);

}
