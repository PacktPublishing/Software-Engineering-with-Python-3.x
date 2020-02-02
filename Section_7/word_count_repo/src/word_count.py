from project_utils import dict_to_file, get_word_count


if __name__ == "__main__":
	
    inp_filename = 'sample.txt'
    
    out_filename = 'count.csv'

    print("Reading file ", inp_filename)

    word_dict = get_word_count(inp_filename)

    print("Output from get_word_count is")
    print(word_dict)

    print("Writing to file named", out_filename)

    dict_to_file(word_dict, out_filename)

    print("Done processing!")
