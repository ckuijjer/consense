

from aenum import Enum


class Data_Enum(Enum):

	_init_ = 'value string'

	NAME = 0, 'name'
	AGE = 1, 'age'
	LOCATION = 2, 'location'
	GENER = 3, 'gender'
	HEIGHT = 4, 'height'
	WEIGHT = 5, 'weight'
	ECG = 6, 'ecg'
	BLOOD = 7, 'blood'
	DNA = 8, 'dna'
	EEG = 9, 'eeg'
	CT = 10, 'ct'

	def __str__(self):
		return self.string

	@classmethod
	def _missing_value_(cls, value):
		for member in cls:
			if member.string == value:
				return member

