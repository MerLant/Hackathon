import { FileUpload } from "@ark-ui/solid/file-upload";
import { For, createSignal } from "solid-js";
import "./UploadFile.css";
import { BiSolidCloudUpload } from "solid-icons/bi";

// https://solid-icons.vercel.app/search/package/bi
export default function UploadFile() {
	return (
		<FileUpload.Root
			maxFiles={5}
			accept="image/*"
			maxFileSize={30 * 1024 * 1024}
		>
			<FileUpload.Label>Загрузить файл</FileUpload.Label>
			<FileUpload.Dropzone>
				<BiSolidCloudUpload size={84} />
			</FileUpload.Dropzone>
			<FileUpload.Trigger>Обработать</FileUpload.Trigger>
			<FileUpload.ItemGroup>
				<FileUpload.Context>
					{(context: () => { acceptedFiles: File[] }) => (
						<>
							<For each={context().acceptedFiles}>
								{(file) => (
									<FileUpload.Item file={file}>
										<FileUpload.ItemPreview type="image/*">
											<FileUpload.ItemPreviewImage />
										</FileUpload.ItemPreview>
										<FileUpload.ItemName />
										<FileUpload.ItemSizeText />
										<FileUpload.ItemDeleteTrigger>
											X
										</FileUpload.ItemDeleteTrigger>
									</FileUpload.Item>
								)}
							</For>
						</>
					)}
				</FileUpload.Context>
			</FileUpload.ItemGroup>
			<FileUpload.HiddenInput />
		</FileUpload.Root>
	);
}
