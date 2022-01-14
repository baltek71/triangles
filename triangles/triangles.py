
import argparse
from ast import List
from dataclasses import asdict, dataclass

@dataclass
class Triangle:
    x: int
    y: int
    z: int

    def __post_init__(self):
        if self.x > 0 and self.y > 0 and self.z > 0:
            traingle_types: List[str] = []
            if self.x == self.y == self.z:
                traingle_types.append("equilateral")
            elif self.x != self.y != self.z:
                traingle_types.append("scalene")
            
            sides = asdict(self).values()
            if len(set(sides)) < len(sides):
                traingle_types.append("isosceles")

            print(f"Triangle is {', '.join(ttype for ttype in traingle_types)}")
        else:
            raise ValueError("Triangle has invalid sides!")

def main():
    parser = argparse.ArgumentParser(description='Create your own triangle')
    parser.add_argument('sidex', type=int, help='Triangle x side')
    parser.add_argument('sidey', type=int, help='Triangle y side')
    parser.add_argument('sidez', type=int, help='Triangle z side')
    args = parser.parse_args()

    Triangle(args.sidex, args.sidey, args.sidez)


if __name__ == '__main__':
    main()