import { splitProps } from "solid-js";
import styles from "./Button.module.css";

type ButtonProps = {
  children: any;
  class?: string;
  variant?: "primary" | "secondary";
  size?: "small" | "medium" | "large";
  onClick?: () => void;
  type?: "button" | "submit" | "reset";
  disabled?: boolean;
};

export default function Button(props: ButtonProps) {
  const [local, others] = splitProps(props, [
    "children",
    "class",
    "variant",
    "size",
  ]);

  return (
    <button
      class={`${styles.button} ${styles[local.variant || "primary"]} ${styles[local.size || "medium"]} ${local.class || ""}`}
      {...others}
    >
      {local.children}
    </button>
  );
}
