from typing import *
from tabulate import tabulate
import random
import analyzer as an
import dictionary
from colr import color
import pyfiglet

CM = NewType("CM", Dict[str, Tuple[Tuple[int, int, int], Tuple[int, int, int]]])

def random_color() -> Tuple[int, int, int]:
    fst = random.randrange(0, 255)
    snd = random.randrange(0, 255)
    thrd = random.randrange(0, 255)
    return (fst, snd, thrd)

def determine_color(tokenized_sentence: List[str]) -> CM:
    # assign each word a random color for easy reading
    colormap: Dict[str, Tuple[int, int, int]] = {}
    for w in tokenized_sentence:
        colormap[w] = (random_color(), random_color())
    return colormap 

def print_colored_sequence(tokens: List[str], colormap: CM) -> None:
    for t in tokens:
        rgb_fore, rgb_back = colormap[t]
        colored_txt = color(t, fore=rgb_fore, back=rgb_back)
        print(colored_txt + " ", end="")
    print()

def print_analysis(one_analysis: Dict[str, str], colormap: CM) -> None:
    orig_txt = one_analysis["orig_text"]
    divider =  "\n" + ("".join((["-"] * 40)))
    c_fore, c_back = colormap[orig_txt]
    print(color(divider, fore=c_fore, back=c_back))
    token_str = "TOKEN: " + orig_txt
    data = [
        [token_str],
    ]

    c = 0
    for k, v in one_analysis.items():
        v = v.lower()

        if k != "ORIG_TEXT":
            k = k.upper()
            text = f"• {k}: " + v
            if c % 3 == 0:
                data.append([text])
            else:
                data[-1].append(text)
        c += 1
    print(color(tabulate(data, tablefmt="fancy_grid"), fore=c_fore))

    

def display(analyzed_sent: List[Dict[str, str]]) -> None:
    tok_sent: List[str] = [token["orig_text"] for token in analyzed_sent]
    colormap: Dict[str, Tuple[int, int, int]] = determine_color(tok_sent)
    print_colored_sequence(tok_sent, colormap)
    for word_data in analyzed_sent:
        print_analysis(word_data, colormap)


def main():
    ascii_banner = pyfiglet.figlet_format("Momus")
    print(color(ascii_banner, fore=(51, 153, 255), back=(0, 0, 0)))
    print(color("Welcome to the Momus translation aid environment.", fore=(102, 255, 255), back=(0, 0, 0)))

    #lat_eng_dict = dictionary.Dictionary()
    analyzer = an.Analyzer()

    while True:
        print(color("Please enter a sentence for analysis below:", fore=(102, 255, 255), back=(0, 0, 0)))
        sentence = input(">>\t")
        analyzed = analyzer.analyze(sentence)
        display(analyzed)

        print(color("----------------------------------------------", fore=(102, 255, 255), back=(0, 0, 0)))

if __name__ == "__main__":
    main()