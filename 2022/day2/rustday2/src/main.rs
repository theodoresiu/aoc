use std::collections::HashMap;
use std::fs::File;
use std::io::{self, BufReader, BufRead};


fn main() {
    let file_path = "../input.txt";
    let file = File::open(file_path).unwrap();

    let reader = BufReader::new(file);
    let mut curr_score1 = 0;
    let mut curr_score2 = 0;

    let sign_translation =  HashMap::from([
        ("A", "X"),
        ("B", "Y"),
        ("C", "Z")]);
    let opp_wins = HashMap::from([
        ("A","Z"),("B","X"),("C","Y")
    ]);
    let opp_loses = HashMap::from([
        ("A","Y"),("B","Z"),("C","X")
    ]);
    let sign_score = HashMap::from(
        [("Y",2),("Z",3),("X",1)]
    );

    for line in reader.lines() {
        let mut line_string = line.unwrap();
        if line_string.ends_with("\n"){
            line_string.pop();
        }
        let signs: Vec<&str> = line_string.split(" ").collect();
        let opp = signs[0];
        let you =signs[1];

        curr_score1 = curr_score1 + sign_score.get(you).unwrap();
        if sign_translation.get(opp).unwrap() == &you {
            curr_score1 = curr_score1 + 3;
        }
        else if opp_wins.get(opp).unwrap() != &you {
            curr_score1 = curr_score1 + 6
        }

        if you == "Y"{
            curr_score2 = curr_score2 + 3;
            let trans1 = sign_translation.get(opp).unwrap();
            curr_score2 = curr_score2 + sign_score.get(trans1).unwrap();
    
        }
        else if you=="X"{
            let trans1 = opp_wins.get(opp).unwrap();
            curr_score2 = curr_score2 + sign_score.get(trans1).unwrap();
        }
        else{
            curr_score2 = curr_score2 + 6;
            let trans1 = opp_loses.get(opp).unwrap();
            curr_score2 = curr_score2 + sign_score.get(trans1).unwrap();
        }

    }
    println!("Here is my initial score {}", curr_score1);
    println!("Here is my other score {}", curr_score2);

    

}
