import os
import shutil
from urllib.parse import unquote, urlparse

import supervisely as sly
import tqdm
from dataset_tools.convert import unpack_if_archive
from supervisely.io.fs import get_file_name, get_file_size

import src.settings as s

# def download_dataset(teamfiles_dir: str) -> str:
#     """Use it for large datasets to convert them on the instance"""
#     api = sly.Api.from_env()
#     team_id = sly.env.team_id()
#     storage_dir = sly.app.get_data_dir()

#     if isinstance(s.DOWNLOAD_ORIGINAL_URL, str):
#         parsed_url = urlparse(s.DOWNLOAD_ORIGINAL_URL)
#         file_name_with_ext = os.path.basename(parsed_url.path)
#         file_name_with_ext = unquote(file_name_with_ext)

#         sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
#         local_path = os.path.join(storage_dir, file_name_with_ext)
#         teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)
#         fsize = get_file_size(local_path)
#         with tqdm(desc=f"Downloading '{file_name_with_ext}' to buffer..", total=fsize) as pbar:
#             api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)
#         dataset_path = unpack_if_archive(local_path)

#     if isinstance(s.DOWNLOAD_ORIGINAL_URL, dict):
#         for file_name_with_ext, url in s.DOWNLOAD_ORIGINAL_URL.items():
#             local_path = os.path.join(storage_dir, file_name_with_ext)
#             teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

#             if not os.path.exists(get_file_name(local_path)):
#                 fsize = get_file_size(local_path)
#                 with tqdm(
#                     desc=f"Downloading '{file_name_with_ext}' to buffer {local_path}...",
#                     total=fsize,
#                     unit="B",
#                     unit_scale=True,
#                 ) as pbar:
#                     api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)

#                 sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
#                 unpack_if_archive(local_path)
#             else:
#                 sly.logger.info(
#                     f"Archive '{file_name_with_ext}' was already unpacked to '{os.path.join(storage_dir, get_file_name(file_name_with_ext))}'. Skipping..."
#                 )

#         dataset_path = storage_dir
#     return dataset_path


# projects = [
#     "/mnt/c/users/german/documents/strawberries/training",
#     "/mnt/c/users/german/documents/strawberries/validation",
# ]

# directory = os.path.dirname(projects[0])
# with open(directory + "/names.txt") as names_file:
#     names = names_file.read().split("\n")


# def yolobbox2bbox(x, y, w, h):
#     x1, y1 = x - w / 2, y - h / 2
#     x2, y2 = x + w / 2, y + h / 2
#     return x1, y1, x2, y2


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    pass


#     project = api.project.create(workspace_id, project_name)
#     meta = sly.ProjectMeta()

#     def load_image_labels(image_path, labels_path):
#         image_info = api.image.upload_path(dataset.id, os.path.basename(image_path), image_path)
#         output = []
#         with open(labels_path) as file:
#             file_split = file.read().rstrip().split("\n")
#         for row in file_split:
#             if row == "":
#                 continue
#             output.append(row.split())
#         labels = []
#         height = image_info.height
#         width = image_info.width
#         for bbox in output:
#             c, x, y, w, h = bbox
#             obj_class_name = names[int(c)]

#             x1, y1, x2, y2 = yolobbox2bbox(float(x), float(y), float(w), float(h))
#             bbox_annotation = sly.Rectangle(y1 * height, x1 * width, y2 * height, x2 * width)
#             obj_class = meta.get_obj_class(obj_class_name)
#             label = sly.Label(bbox_annotation, obj_class)
#             labels.append(label)

#         ann = sly.Annotation(img_size=[height, width], labels=labels)
#         api.annotation.upload_ann(image_info.id, ann)

#     for name in names:
#         if name == "":
#             break
#         obj_class = sly.ObjClass(name, sly.Rectangle)
#         meta = meta.add_obj_class(obj_class)
#         api.project.update_meta(project.id, meta)

#     for project_directory in projects:
#         image_path = sly.fs.list_files(project_directory, valid_extensions=[".jpg"])
#         dataset = api.dataset.create(project.id, os.path.basename(project_directory))
#         # upload bboxes to images
#         pbar = tqdm.tqdm(desc="image", total=len(image_path))
#         for path in image_path:
#             l_path = os.path.join(project_directory, (os.path.basename(path)[:-4] + ".txt"))
#             load_image_labels(path, l_path)
#             pbar.update(1)
#         pbar.close()
#         print(f"Dataset {dataset.id} has been successfully created.")

#     return project
