import { Field } from "@ark-ui/solid/field";
import Button from "../Button/Button";

export default function Input() {
  return (
    <Field.Root>
      <Field.Label>Поиск по мета-данным</Field.Label>
      <Field.Input />
      <Field.HelperText>Some additional Info</Field.HelperText>
      <Button
        variant="secondary"
        size="small"
        onClick={() => console.log("Clicked!")}
      >
        Click me
      </Button>
      <Field.ErrorText>Error Info</Field.ErrorText>
    </Field.Root>
  );
}
