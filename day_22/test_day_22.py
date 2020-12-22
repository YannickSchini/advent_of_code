import unittest
import day_22


class testDay22(unittest.TestCase):
    def test_part_1(self):
        # Given
        test_filepath = "test_file.txt"
        # When
        result = day_22.part_1(test_filepath)
        # Then
        self.assertEqual(result, 306)

    def test_parse_inputs(self):
        # Given
        test_filepath = "test_file.txt"
        # When
        player_1_deck, player_2_deck = day_22.parse_inputs(test_filepath)
        # Then
        self.assertEqual(player_1_deck, [9, 2, 6, 3, 1])
        self.assertEqual(player_2_deck, [5, 8, 4, 7, 10])

    def test_play_one_turn(self):
        # Given
        test_filepath = "test_file.txt"
        player_1_deck, player_2_deck = day_22.parse_inputs(test_filepath)
        # When
        player_1_deck_after_1_turn, player_2_deck_after_1_turn = \
            day_22.play_one_turn(player_1_deck, player_2_deck)
        player_1_deck_after_2_turn, player_2_deck_after_2_turn = \
            day_22.play_one_turn(player_1_deck_after_1_turn,
                                 player_2_deck_after_1_turn)
        # Then
        self.assertEqual(player_1_deck_after_1_turn, [2, 6, 3, 1, 9, 5])
        self.assertEqual(player_2_deck_after_1_turn, [8, 4, 7, 10])
        self.assertEqual(player_1_deck_after_2_turn, [6, 3, 1, 9, 5])
        self.assertEqual(player_2_deck_after_2_turn, [4, 7, 10, 8, 2])

    def test_play_one_game(self):
        # Given
        test_filepath = "test_file.txt"
        player_1_deck, player_2_deck = day_22.parse_inputs(test_filepath)
        # When
        number_of_turns, winning_deck = day_22.play_one_game(
            player_1_deck, player_2_deck)
        # Then
        self.assertEqual(number_of_turns, 29)
        self.assertEqual(winning_deck, [3, 2, 10, 6, 8, 5, 9, 4, 7, 1])

    def test_calculate_score(self):
        # Given
        player_deck = [3, 2, 10, 6, 8, 5, 9, 4, 7, 1]
        # When
        score = day_22.calculate_score(player_deck)
        # Then
        self.assertEqual(score, 306)


if __name__ == "__main__":
    unittest.main()
