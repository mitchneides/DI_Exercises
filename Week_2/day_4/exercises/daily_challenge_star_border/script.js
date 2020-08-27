
function get_longest_word_length(words) {	
	let longest_length = 0;
	for (current_word of words) {
		if (current_word.length > longest_length) {
			longest_length = current_word.length;
		}
	}
	return longest_length;
}


function create_box() {
	let sentence = prompt("Enter a sentence: ");
	let words = sentence.split(" ");

	// create top and bottom border according to size of longest word
	let longest_length = get_longest_word_length(words);
	let border = ("*").repeat(longest_length+4)
	border = border + "\n";

	//on a new line every time, prints star, space, the word, fills the rest of the space and ends with a *
	let middle_stuff = "";
	for (current_word of words) {
		middle_stuff = middle_stuff+ "* " +current_word + (" ").repeat(longest_length - current_word.length) + " *" + "\n";
	}

	return (border + middle_stuff + border);
}


console.log(create_box());


