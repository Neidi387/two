use std::fs

fn main() {
    let input = fs::read_to_string("input.txt").expect("Could not read file");
    let reports = get_reports(input);
}

fn get_reports(input: String) -> Vec<Vec<u16>> {
    let lines = input.split("\n");
    let reportStrs = lines.map(|line| line.split(" "));
    reportsStrs.map(|reportStr| reportStr)
}