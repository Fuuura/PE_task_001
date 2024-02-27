from subprocess import run, PIPE
import os
import pytest

B_FILE_PATH = './src/roman_to_arabic'


def test_roman_to_arabic_MMXXIV():
    result = run([B_FILE_PATH], input='MMXXIV', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert int(result.stdout.strip()) == 2024

def test_roman_to_arabic_MCMLXXXIX():
    result = run([B_FILE_PATH], input='MCMLXXXIX', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert int(result.stdout.strip()) == 1989

def test_roman_to_arabic_MMCCLXXXVIII():
    result = run([B_FILE_PATH], input='MMCCLXXXVIII', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert int(result.stdout.strip()) == 2288


def test_roman_to_arabic_I():
    result = run([B_FILE_PATH], input='I', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert int(result.stdout.strip()) == 1


def test_roman_to_arabic_II():
    result = run([B_FILE_PATH], input='II', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert int(result.stdout.strip()) == 2


def test_roman_to_arabic_nulla():
    result = run([B_FILE_PATH], input='nulla', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert int(result.stdout.strip()) == 0


def test_roman_to_arabic_nihil():
    result = run([B_FILE_PATH], input='nihil', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert int(result.stdout.strip()) == 0


def test_roman_to_arabic_N():
    result = run([B_FILE_PATH], input='N', encoding='utf-8', stdout=PIPE)
    assert result.returncode == 0
    assert int(result.stdout.strip()) == 0


def test_src_folder_contains_roman_to_arabic_c():
    assert os.path.isfile('./src/roman_to_arabic.c')


def test_src_folder_contains_roman_to_arabic_c_correct_name():
    assert os.path.basename('./src/roman_to_arabic.c') == 'roman_to_arabic.c'


def test_roman_to_arabic_not_correct_input_1():
    result = run([B_FILE_PATH], input='01', encoding='utf-8', stdout=PIPE, stderr=PIPE)
    assert result.returncode != 0
    assert "Puck you, Verter!" in result.stderr


def test_roman_to_arabic_not_correct_input_2():
    result = run([B_FILE_PATH], input='wehlkj', encoding='utf-8', stdout=PIPE, stderr=PIPE)
    assert result.returncode != 0
    assert "Puck you, Verter!" in result.stderr


def test_roman_to_arabic_not_correct_input_3():
    result = run([B_FILE_PATH], input='0', encoding='utf-8', stdout=PIPE, stderr=PIPE)
    assert result.returncode != 0
    assert "Puck you, Verter!" in result.stderr

def test_roman_to_arabic_not_correct_input_4():
    result = run([B_FILE_PATH], input='CMCMIXIX', encoding='utf-8', stdout=PIPE, stderr=PIPE)
    assert result.returncode != 0
    assert "Puck you, Verter!" in result.stderr

if __name__ == "__main__":
    pytest.main()
