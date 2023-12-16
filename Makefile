.PHONY : all all-offline fetch-and-postprocess-proto-files postprocess fetch clean-offline

all:
	$(MAKE) fetch-proto-files
	$(MAKE) all-offline

all-offline:
	$(MAKE) postprocess-proto-files
	$(MAKE) generate-py
	$(MAKE) postprocess-py

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
