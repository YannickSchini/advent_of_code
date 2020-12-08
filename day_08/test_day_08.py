import unittest
import day_08


class testBootCodeChecker(unittest.TestCase):
    def test_process_instruction_handles_different_cases(self):
        # Given
        input_acc = "acc +3"
        input_jmp = "jmp -11"
        input_nop = "nop +0"
        # When
        result_acc = day_08.process_instruction(input_acc)
        result_jmp = day_08.process_instruction(input_jmp)
        result_nop = day_08.process_instruction(input_nop)
        # Then
        self.assertEqual(result_acc, (3, 1))
        self.assertEqual(result_jmp, (0, -11))
        self.assertEqual(result_nop, (0, 1))

    def test_process_boot_code_processes_looping_example_file_correctly(self):
        # Given
        file = "test_file_with_loop.txt"
        with open(file, "r") as boot_loader_code:
            instruction_list = boot_loader_code.readlines()
        # When
        exit_status, accumulator = day_08.process_boot_code(instruction_list)
        # Then
        self.assertEqual(accumulator, 5)

    def test_process_boot_code_processes_no_loop_example_file_correctly(self):
        # Given
        file = "test_file_without_loop.txt"
        with open(file, "r") as boot_loader_code:
            instruction_list = boot_loader_code.readlines()
        # When
        exit_status, accumulator = day_08.process_boot_code(instruction_list)
        # Then
        self.assertEqual(accumulator, 8)

    def test_fix_bootloader_returns_correct_accumulator_value(self):
        # Given
        file = "test_file_with_loop.txt"
        with open(file, "r") as boot_loader_code:
            instruction_list = boot_loader_code.readlines()
        # When
        exit_status, accumulator = day_08.fix_bootloader(instruction_list)
        # Then
        self.assertTrue(accumulator, 8)


if __name__ == "__main__":
    unittest.main()
