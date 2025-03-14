import { Title } from "@solidjs/meta";
import UploadFile from "~/components/UploadFile/UploadFile";
import Field from "~/components/Search/Search";

export default function Home() {
	return (
		<main>
			<Title>HshCode</Title>
			<h1>Команда HSHCODE</h1>
			<Field />
			<UploadFile />
		</main>
	);
}
