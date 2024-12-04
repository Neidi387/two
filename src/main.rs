use std::fs;

fn main() {
    let input = fs::read_to_string("input.txt").expect("Could not read file");
    let reports = get_reports(input);
    let reports_correct: Vec<_> = reports.iter().filter(is_success).collect();
    let correct_reports_count = reports_correct.len();
    print!("Correct Reports: {correct_reports_count}")
}

fn get_reports(input: String) -> Vec<Vec<i16>> {
    let lines_it = input.split("\n");
    let reports: Vec<_> = lines_it.map(split_whitespace_and_parse).collect();
    return reports
}

fn is_success(report: &&Vec<i16>) -> bool {
    let mut last_diff = report[1] - report[0];
    if last_diff.abs() < 1 || last_diff.abs() > 3 {
        return false;
    }
    for i in 1..report.len() - 1 {
        let diff = report[i+1] - report[i];
        if diff.abs() < 1 || diff.abs() > 3 {
            return false;
        }
        if last_diff < 0 && diff > 0 {
            return false;
        }
        if last_diff > 0 && diff < 0 {
            return  false;
        }
        last_diff = diff;
    }
    return true;
}

fn split_whitespace_and_parse(line: &str) -> Vec<i16> {
    let numbers = line.split(" ").map(|value| 
        value.parse::<i16>().expect("Wasnt able to parse level")
    ).collect();
    return numbers;
}