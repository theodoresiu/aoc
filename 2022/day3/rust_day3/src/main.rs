use std::collections::HashSet;
use std::fs::File;
use std::io::{self, BufReader, BufRead};


pub fn process_two(s1: &str, s2: &str) -> Option<char>{
    let set1: HashSet<char> = s1.chars().collect();
    let set2: HashSet<char> = s2.chars().collect();
    let result = set1.intersection(&set2).last().unwrap().to_owned();
    Some(result)
}

pub fn process_three(s1: &str, s2: &str, s3: &str) -> Option<char>{
    let set1: HashSet<char> = s1.chars().collect();
    let set2: HashSet<char> = s2.chars().collect();
    let set3: HashSet<char> = s3.chars().collect();

    let r1 = set1.intersection(&set2).find(|it| set3.contains(it)).unwrap().to_owned();
    Some(r1)
}

pub fn calc_score(c: char) -> i32{
    let value = c as i32;
    if c.is_lowercase(){
        return value - 96
    }
    return value-64+26

}

fn main() {
    let file_path = "../input.txt";
    let file = File::open(file_path).unwrap();

    let reader = BufReader::new(file);
    let mut curr_score1 = 0;
    let mut curr_score2 = 0;

    let lines: Vec<String> = reader.lines().collect::<Result<_, _>>().unwrap();
    let otherlines = lines.clone();
    let otherlines: Vec<&[String]> = otherlines.chunks(3).collect();
   
    
    for line in lines{
        let (p1, p2) = line.split_at(line.len()/2);
        let result = process_two(p1, p2).unwrap();
        curr_score1 = curr_score1 + calc_score(result)

    }

    for three in otherlines{
        if three.len() == 3{
        let result = process_three(&three[0], &three[1], &three[2]).unwrap();
        curr_score2 = curr_score2 + calc_score(result);
        }

    }

    println!("First result {}", curr_score1);
    println!("Second result {}", curr_score2);



    
}
