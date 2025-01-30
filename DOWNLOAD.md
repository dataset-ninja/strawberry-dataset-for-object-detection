Dataset **Strawberry Dataset for Object Detection** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzEzNjBfU3RyYXdiZXJyeSBEYXRhc2V0IGZvciBPYmplY3QgRGV0ZWN0aW9uL3N0cmF3YmVycnktZGF0YXNldC1mb3Itb2JqZWN0LWRldGVjdGlvbi1EYXRhc2V0TmluamEudGFyIiwgInNpZyI6ICJ1em5HbTQwNkljazNTSW9Nd3NUSi9oR3dUOVNiZGIxVDF0bjZOcGhIUVFjPSJ9)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Strawberry Dataset for Object Detection', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://zenodo.org/record/6126677/files/strawberries.zip?download=1).