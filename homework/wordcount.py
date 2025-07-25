# obtain a list of files in the input directory
import os


def main():

    input_file_list = os.listdir("data/input/")

    # count the frequency of the words in the files in the input directory
    counter = {}
    for filename in input_file_list:
        with open("data/input/" + filename) as f:
            for l in f:
                for w in l.split():
                    w = w.lower().strip(",.!?")
                    counter[w] = counter.get(w, 0) + 1

    # create the directory output/ if it doesn't exist
    if not os.path.exists("data/output"):
        os.makedirs("data/output")

    # save the results using tsv format
    with open("data/output/results.tsv", "w", encoding="utf-8") as f:
        for key, value in counter.items():
            # write the key and value to the file
            f.write(f"{key}\t{value}\n")


if __name__ == "__main__":
    main()


    # obtain a list of files in the input directory

#import sys

#from ._internals.count_words import count_words
#from ._internals.preprocess_lines import preprocess_lines
#from ._internals.read_all_lines import read_all_lines
#from ._internals.split_into_words import split_into_words
#from ._internals.write_word_counts import write_word_counts


#def main():

    #if len(sys.argv) != 3:
        #print("Usage: python3 -m homework <input_folder> <output_folder>")
        #sys.exit(1)

    #input_folder = sys.argv[1]
    #output_folder = sys.argv[2]

    #all_lines = read_all_lines(input_folder)
    #all_lines = preprocess_lines(all_lines)
    #words = split_into_words(all_lines)
    #counter = count_words(words)
    #write_word_counts(counter, output_folder)


#if __name__ == "__main__":
    #main()