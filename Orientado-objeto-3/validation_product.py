class Validation:
    def validation_string_input(self, input_string):
        if type(input_string) == str:
            validated_price = float(input_string.replace('R$', ''))
            return validated_price
        else:
            return input_string
