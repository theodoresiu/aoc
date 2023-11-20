use std::fs::File;
use std::io::{self, BufReader, BufRead};

pub fn get_range(s: &str) -> (i32, i32){
    let result: Vec<&str> = s.split("-").collect();
    let p1 = result[0].parse::<i32>().unwrap();
    let p2 = result[1].parse::<i32>().unwrap();
    return (p1,p2)

}

fn main() {
    let file_path = "../input.txt";
    let file = File::open(file_path).unwrap();

    let reader = BufReader::new(file);
    let mut curr_score1 = 0;
    let mut curr_score2 = 0;

    for line in reader.lines() {
        let line_string = line.unwrap();
        let ranges: Vec<&str> = line_string.split(",").collect();
        let r1 = ranges[0];
        let r2 = ranges[1];
        let (x1, x2) = get_range(r1);
        let (y1, y2) = get_range(r2);

        if (x1<=y1 && x2>=y2) || (y1<=x1 && y2>=x2){
        curr_score1 =  curr_score1+1;
        }
    if (x1<=y1 && x2>=y1) || (y1<=x1 && y2>=x1){
        curr_score2 = curr_score2 +1
    }
    }
    println!("{}", curr_score1);
    println!("{}", curr_score2);


}
