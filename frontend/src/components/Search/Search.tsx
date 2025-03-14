import { Field } from "@ark-ui/solid/field";

export default function Input() {
	return (
		<Field.Root>
			<Field.Label>Поиск по мета-данным</Field.Label>
			<Field.Input />
			<Field.HelperText>Some additional Info</Field.HelperText>
			<Field.ErrorText>Error Info</Field.ErrorText>
		</Field.Root>
	);
}
