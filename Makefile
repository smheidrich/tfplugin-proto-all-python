.PHONY : all all-offline fetch-and-postprocess-proto-files postprocess fetch clean-offline

all:
	$(MAKE) fetch-proto-files
	$(MAKE) all-offline

all-offline:
	$(MAKE) postprocess-proto-files
	$(MAKE) generate-py
	$(MAKE) postprocess-py
	$(MAKE) package-struct-py

package-struct-py:
	./make-py-package-structure.sh

postprocess-py:
	./postprocess-generated-py.sh

generate-py:
	./generate-py.sh

postprocess-proto-files:
	./postprocess-proto-files.sh

fetch-proto-files:
	./fetch-proto-files-from-tf-repo.sh

clean-offline:
	rm -rf ./postprocessed_proto_files
	rm -rf ./generated_python_files
	rm -rf ./postprocessed_python_files
	rm -rf ./tfplugin_proto/*.py*
