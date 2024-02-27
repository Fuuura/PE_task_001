from subprocess import run, PIPE
import os
import os.path
import pytest

B_FILE_PATH = './src/universal_convert'

if os.path.isfile(B_FILE_PATH):

    def test_universal_convert_MMXXIV():
        result = run([B_FILE_PATH], input='1 MMXXIV', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert int(result.stdout.strip()) == 2024
    
    def test_universal_convert_2024():
        result = run([B_FILE_PATH], input='2 2024', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout.strip() == 'MMXXIV'

    def test_universal_convert_MCMLXXXIX():
        result = run([B_FILE_PATH], input='1 MCMLXXXIX', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert int(result.stdout.strip()) == 1989
    
    def test_universal_convert_1989():
        result = run([B_FILE_PATH], input='2 1989', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout.strip() == 'MCMLXXXIX'

    def test_universal_convert_MMCCLXXXVIII():
        result = run([B_FILE_PATH], input='1 MMCCLXXXVIII', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert int(result.stdout.strip()) == 2288
    
    def test_universal_convert_2288():
        result = run([B_FILE_PATH], input='2 2288', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout.strip() == 'MMCCLXXXVIII'


    def test_universal_convert_I():
        result = run([B_FILE_PATH], input='1 I', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert int(result.stdout.strip()) == 1

    def test_universal_convert_1():
        result = run([B_FILE_PATH], input='2 1', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout.strip() == 'I'


    def test_universal_convert_II():
        result = run([B_FILE_PATH], input='1 II', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert int(result.stdout.strip()) == 2
    
    def test_universal_convert_2():
        result = run([B_FILE_PATH], input='2 2', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert result.stdout.strip() == 'II'


    def test_universal_convert_nulla():
        result = run([B_FILE_PATH], input='1 nulla', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert int(result.stdout.strip()) == 0


    def test_universal_convert_nihil():
        result = run([B_FILE_PATH], input='1 nihil', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert int(result.stdout.strip()) == 0


    def test_universal_convert_N():
        result = run([B_FILE_PATH], input='1 N', encoding='utf-8', stdout=PIPE)
        assert result.returncode == 0
        assert int(result.stdout.strip()) == 0


    def test_src_folder_contains_universal_convert_c():
        assert os.path.isfile('./src/universal_convert.c')


    def test_src_folder_contains_universal_convert_c_correct_name():
        assert os.path.basename('./src/universal_convert.c') == 'universal_convert.c'


    def test_universal_convert_not_correct_input_1():
        result = run([B_FILE_PATH], input='1 01', encoding='utf-8', stdout=PIPE, stderr=PIPE)
        assert result.returncode != 0
        assert "Puck you, Verter!" in result.stderr


    def test_universal_convert_not_correct_input_2():
        result = run([B_FILE_PATH], input='1 wehlkj', encoding='utf-8', stdout=PIPE, stderr=PIPE)
        assert result.returncode != 0
        assert "Puck you, Verter!" in result.stderr


    def test_universal_convert_not_correct_input_3():
        result = run([B_FILE_PATH], input='1 0', encoding='utf-8', stdout=PIPE, stderr=PIPE)
        assert result.returncode != 0
        assert "Puck you, Verter!" in result.stderr
    
    def test_universal_convert_not_correct_input_4():
        result = run([B_FILE_PATH], input='0', encoding='utf-8', stdout=PIPE, stderr=PIPE)
        assert result.returncode != 0
        assert "Puck you, Verter!" in result.stderr
    
    def test_universal_convert_not_correct_input_5():
        result = run([B_FILE_PATH], input='2 0', encoding='utf-8', stdout=PIPE, stderr=PIPE)
        if result.returncode == 0:
            assert result.stdout.strip() == 'nihil' or result.stdout.strip() == 'nulla' or result.stdout.strip() == 'N'
    
    def test_universal_convert_not_correct_input_6():
        result = run([B_FILE_PATH], input='2 -1', encoding='utf-8', stdout=PIPE, stderr=PIPE)
        assert result.returncode != 0
        assert "Puck you, Verter!" in result.stderr
    
    def test_universal_convert_not_correct_input_7():
        result = run([B_FILE_PATH], input='1 CMCMIXIX', encoding='utf-8', stdout=PIPE, stderr=PIPE)
        assert result.returncode != 0
        assert "Puck you, Verter!" in result.stderr

if __name__ == "__main__":
    pytest.main()
