fn main() {
    println!("Hello, world!");
}

fn queensAttack(n: i32, k: i32, r_q: i32, c_q: i32, obstacles: &[Vec<i32>]) -> i32 {
    let diagonal = r_q - c_q;
    let anti_diagonal = r_q + c_q;

    let obstacles = obstacles
        .into_iter()
        .filter(|&o| {
            let (r, c) = (o[0], o[1]);

            r == r_q || c == c_q || r - c == diagonal || r + c == anti_diagonal
        })
        .collect::<Vec<_>>();

    let mut count = 0;
    for d in [
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
    ] {
        let (mut r, mut c) = (r_q, c_q);
        loop {
            r += d.0;
            c += d.1;

            if c > n || c < 1 || r > n || r < 1 || obstacles.contains(&&vec![r, c]) {
                break;
            }

            count += 1;
        }
    }

    count
}
