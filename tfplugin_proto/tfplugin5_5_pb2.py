# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tfplugin5_5.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11tfplugin5_5.proto\x12\ttfplugin5\"-\n\x0c\x44ynamicValue\x12\x0f\n\x07msgpack\x18\x01 \x01(\x0c\x12\x0c\n\x04json\x18\x02 \x01(\x0c\"\xf3\x01\n\nDiagnostic\x12\x30\n\x08severity\x18\x01 \x01(\x0e\x32\x1e.tfplugin5.Diagnostic.Severity\x12\x0f\n\x07summary\x18\x02 \x01(\t\x12\x0e\n\x06\x64\x65tail\x18\x03 \x01(\t\x12+\n\tattribute\x18\x04 \x01(\x0b\x32\x18.tfplugin5.AttributePath\x12\x1e\n\x11\x66unction_argument\x18\x05 \x01(\x03H\x00\x88\x01\x01\"/\n\x08Severity\x12\x0b\n\x07INVALID\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x12\x0b\n\x07WARNING\x10\x02\x42\x14\n\x12_function_argument\"\xa4\x01\n\rAttributePath\x12,\n\x05steps\x18\x01 \x03(\x0b\x32\x1d.tfplugin5.AttributePath.Step\x1a\x65\n\x04Step\x12\x18\n\x0e\x61ttribute_name\x18\x01 \x01(\tH\x00\x12\x1c\n\x12\x65lement_key_string\x18\x02 \x01(\tH\x00\x12\x19\n\x0f\x65lement_key_int\x18\x03 \x01(\x03H\x00\x42\n\n\x08selector\",\n\x04Stop\x1a\t\n\x07Request\x1a\x19\n\x08Response\x12\r\n\x05\x45rror\x18\x01 \x01(\t\"{\n\x08RawState\x12\x0c\n\x04json\x18\x01 \x01(\x0c\x12\x31\n\x07\x66latmap\x18\x02 \x03(\x0b\x32 .tfplugin5.RawState.FlatmapEntry\x1a.\n\x0c\x46latmapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xe4\x05\n\x06Schema\x12\x0f\n\x07version\x18\x01 \x01(\x03\x12&\n\x05\x62lock\x18\x02 \x01(\x0b\x32\x17.tfplugin5.Schema.Block\x1a\xd7\x01\n\x05\x42lock\x12\x0f\n\x07version\x18\x01 \x01(\x03\x12/\n\nattributes\x18\x02 \x03(\x0b\x32\x1b.tfplugin5.Schema.Attribute\x12\x32\n\x0b\x62lock_types\x18\x03 \x03(\x0b\x32\x1d.tfplugin5.Schema.NestedBlock\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12/\n\x10\x64\x65scription_kind\x18\x05 \x01(\x0e\x32\x15.tfplugin5.StringKind\x12\x12\n\ndeprecated\x18\x06 \x01(\x08\x1a\xca\x01\n\tAttribute\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\x0c\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x10\n\x08required\x18\x04 \x01(\x08\x12\x10\n\x08optional\x18\x05 \x01(\x08\x12\x10\n\x08\x63omputed\x18\x06 \x01(\x08\x12\x11\n\tsensitive\x18\x07 \x01(\x08\x12/\n\x10\x64\x65scription_kind\x18\x08 \x01(\x0e\x32\x15.tfplugin5.StringKind\x12\x12\n\ndeprecated\x18\t \x01(\x08\x1a\xf9\x01\n\x0bNestedBlock\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12&\n\x05\x62lock\x18\x02 \x01(\x0b\x32\x17.tfplugin5.Schema.Block\x12:\n\x07nesting\x18\x03 \x01(\x0e\x32).tfplugin5.Schema.NestedBlock.NestingMode\x12\x11\n\tmin_items\x18\x04 \x01(\x03\x12\x11\n\tmax_items\x18\x05 \x01(\x03\"M\n\x0bNestingMode\x12\x0b\n\x07INVALID\x10\x00\x12\n\n\x06SINGLE\x10\x01\x12\x08\n\x04LIST\x10\x02\x12\x07\n\x03SET\x10\x03\x12\x07\n\x03MAP\x10\x04\x12\t\n\x05GROUP\x10\x05\"P\n\x12ServerCapabilities\x12\x14\n\x0cplan_destroy\x18\x01 \x01(\x08\x12$\n\x1cget_provider_schema_optional\x18\x02 \x01(\x08\"\xd8\x03\n\x08\x46unction\x12\x31\n\nparameters\x18\x01 \x03(\x0b\x32\x1d.tfplugin5.Function.Parameter\x12\x39\n\x12variadic_parameter\x18\x02 \x01(\x0b\x32\x1d.tfplugin5.Function.Parameter\x12*\n\x06return\x18\x03 \x01(\x0b\x32\x1a.tfplugin5.Function.Return\x12\x0f\n\x07summary\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12/\n\x10\x64\x65scription_kind\x18\x06 \x01(\x0e\x32\x15.tfplugin5.StringKind\x12\x1b\n\x13\x64\x65precation_message\x18\x07 \x01(\t\x1a\xa5\x01\n\tParameter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\x0c\x12\x18\n\x10\x61llow_null_value\x18\x03 \x01(\x08\x12\x1c\n\x14\x61llow_unknown_values\x18\x04 \x01(\x08\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12/\n\x10\x64\x65scription_kind\x18\x06 \x01(\x0e\x32\x15.tfplugin5.StringKind\x1a\x16\n\x06Return\x12\x0c\n\x04type\x18\x01 \x01(\x0c\"\xb8\x03\n\x0bGetMetadata\x1a\t\n\x07Request\x1a\xab\x02\n\x08Response\x12:\n\x13server_capabilities\x18\x01 \x01(\x0b\x32\x1d.tfplugin5.ServerCapabilities\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\x12?\n\x0c\x64\x61ta_sources\x18\x03 \x03(\x0b\x32).tfplugin5.GetMetadata.DataSourceMetadata\x12:\n\tresources\x18\x04 \x03(\x0b\x32\'.tfplugin5.GetMetadata.ResourceMetadata\x12:\n\tfunctions\x18\x05 \x03(\x0b\x32\'.tfplugin5.GetMetadata.FunctionMetadata\x1a \n\x10\x46unctionMetadata\x12\x0c\n\x04name\x18\x01 \x01(\t\x1a\'\n\x12\x44\x61taSourceMetadata\x12\x11\n\ttype_name\x18\x01 \x01(\t\x1a%\n\x10ResourceMetadata\x12\x11\n\ttype_name\x18\x01 \x01(\t\"\xbb\x05\n\x11GetProviderSchema\x1a\t\n\x07Request\x1a\x9a\x05\n\x08Response\x12#\n\x08provider\x18\x01 \x01(\x0b\x32\x11.tfplugin5.Schema\x12T\n\x10resource_schemas\x18\x02 \x03(\x0b\x32:.tfplugin5.GetProviderSchema.Response.ResourceSchemasEntry\x12Y\n\x13\x64\x61ta_source_schemas\x18\x03 \x03(\x0b\x32<.tfplugin5.GetProviderSchema.Response.DataSourceSchemasEntry\x12G\n\tfunctions\x18\x07 \x03(\x0b\x32\x34.tfplugin5.GetProviderSchema.Response.FunctionsEntry\x12*\n\x0b\x64iagnostics\x18\x04 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\x12(\n\rprovider_meta\x18\x05 \x01(\x0b\x32\x11.tfplugin5.Schema\x12:\n\x13server_capabilities\x18\x06 \x01(\x0b\x32\x1d.tfplugin5.ServerCapabilities\x1aI\n\x14ResourceSchemasEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12 \n\x05value\x18\x02 \x01(\x0b\x32\x11.tfplugin5.Schema:\x02\x38\x01\x1aK\n\x16\x44\x61taSourceSchemasEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12 \n\x05value\x18\x02 \x01(\x0b\x32\x11.tfplugin5.Schema:\x02\x38\x01\x1a\x45\n\x0e\x46unctionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.tfplugin5.Function:\x02\x38\x01\"\xb5\x01\n\x15PrepareProviderConfig\x1a\x32\n\x07Request\x12\'\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x1ah\n\x08Response\x12\x30\n\x0fprepared_config\x18\x01 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\"\xd6\x01\n\x14UpgradeResourceState\x1aU\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x03\x12&\n\traw_state\x18\x03 \x01(\x0b\x32\x13.tfplugin5.RawState\x1ag\n\x08Response\x12/\n\x0eupgraded_state\x18\x01 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\"\x9b\x01\n\x1aValidateResourceTypeConfig\x1a\x45\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\'\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x1a\x36\n\x08Response\x12*\n\x0b\x64iagnostics\x18\x01 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\"\x99\x01\n\x18ValidateDataSourceConfig\x1a\x45\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\'\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x1a\x36\n\x08Response\x12*\n\x0b\x64iagnostics\x18\x01 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\"\x92\x01\n\tConfigure\x1aM\n\x07Request\x12\x19\n\x11terraform_version\x18\x01 \x01(\t\x12\'\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x1a\x36\n\x08Response\x12*\n\x0b\x64iagnostics\x18\x01 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\"\x93\x02\n\x0cReadResource\x1a\x8d\x01\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12.\n\rcurrent_state\x18\x02 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12\x0f\n\x07private\x18\x03 \x01(\x0c\x12.\n\rprovider_meta\x18\x04 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x1as\n\x08Response\x12*\n\tnew_state\x18\x01 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\x12\x0f\n\x07private\x18\x03 \x01(\x0c\"\xd8\x03\n\x12PlanResourceChange\x1a\xef\x01\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12,\n\x0bprior_state\x18\x02 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12\x33\n\x12proposed_new_state\x18\x03 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12\'\n\x06\x63onfig\x18\x04 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12\x15\n\rprior_private\x18\x05 \x01(\x0c\x12.\n\rprovider_meta\x18\x06 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x1a\xcf\x01\n\x08Response\x12.\n\rplanned_state\x18\x01 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12\x32\n\x10requires_replace\x18\x02 \x03(\x0b\x32\x18.tfplugin5.AttributePath\x12\x17\n\x0fplanned_private\x18\x03 \x01(\x0c\x12*\n\x0b\x64iagnostics\x18\x04 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\x12\x1a\n\x12legacy_type_system\x18\x05 \x01(\x08\"\x96\x03\n\x13\x41pplyResourceChange\x1a\xec\x01\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12,\n\x0bprior_state\x18\x02 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12.\n\rplanned_state\x18\x03 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12\'\n\x06\x63onfig\x18\x04 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12\x17\n\x0fplanned_private\x18\x05 \x01(\x0c\x12.\n\rprovider_meta\x18\x06 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x1a\x8f\x01\n\x08Response\x12*\n\tnew_state\x18\x01 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12\x0f\n\x07private\x18\x02 \x01(\x0c\x12*\n\x0b\x64iagnostics\x18\x03 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\x12\x1a\n\x12legacy_type_system\x18\x04 \x01(\x08\"\xa5\x02\n\x13ImportResourceState\x1a(\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x1a^\n\x10ImportedResource\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12&\n\x05state\x18\x02 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12\x0f\n\x07private\x18\x03 \x01(\x0c\x1a\x83\x01\n\x08Response\x12K\n\x12imported_resources\x18\x01 \x03(\x0b\x32/.tfplugin5.ImportResourceState.ImportedResource\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\"\xe7\x01\n\x0eReadDataSource\x1au\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\'\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12.\n\rprovider_meta\x18\x03 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x1a^\n\x08Response\x12&\n\x05state\x18\x01 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\"\x81\x01\n\x14GetProvisionerSchema\x1a\t\n\x07Request\x1a^\n\x08Response\x12&\n\x0bprovisioner\x18\x01 \x01(\x0b\x32\x11.tfplugin5.Schema\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\"\x87\x01\n\x19ValidateProvisionerConfig\x1a\x32\n\x07Request\x12\'\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x1a\x36\n\x08Response\x12*\n\x0b\x64iagnostics\x18\x01 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\"\xbc\x01\n\x11ProvisionResource\x1a_\n\x07Request\x12\'\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12+\n\nconnection\x18\x02 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x1a\x46\n\x08Response\x12\x0e\n\x06output\x18\x01 \x01(\t\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\"\xdd\x01\n\x0cGetFunctions\x1a\t\n\x07Request\x1a\xc1\x01\n\x08Response\x12\x42\n\tfunctions\x18\x01 \x03(\x0b\x32/.tfplugin5.GetFunctions.Response.FunctionsEntry\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin5.Diagnostic\x1a\x45\n\x0e\x46unctionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.tfplugin5.Function:\x02\x38\x01\"\xb4\x01\n\x0c\x43\x61llFunction\x1a\x43\n\x07Request\x12\x0c\n\x04name\x18\x01 \x01(\t\x12*\n\targuments\x18\x02 \x03(\x0b\x32\x17.tfplugin5.DynamicValue\x1a_\n\x08Response\x12\'\n\x06result\x18\x01 \x01(\x0b\x32\x17.tfplugin5.DynamicValue\x12*\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x15.tfplugin5.Diagnostic*%\n\nStringKind\x12\t\n\x05PLAIN\x10\x00\x12\x0c\n\x08MARKDOWN\x10\x01\x32\x8d\x0b\n\x08Provider\x12N\n\x0bGetMetadata\x12\x1e.tfplugin5.GetMetadata.Request\x1a\x1f.tfplugin5.GetMetadata.Response\x12X\n\tGetSchema\x12$.tfplugin5.GetProviderSchema.Request\x1a%.tfplugin5.GetProviderSchema.Response\x12l\n\x15PrepareProviderConfig\x12(.tfplugin5.PrepareProviderConfig.Request\x1a).tfplugin5.PrepareProviderConfig.Response\x12{\n\x1aValidateResourceTypeConfig\x12-.tfplugin5.ValidateResourceTypeConfig.Request\x1a..tfplugin5.ValidateResourceTypeConfig.Response\x12u\n\x18ValidateDataSourceConfig\x12+.tfplugin5.ValidateDataSourceConfig.Request\x1a,.tfplugin5.ValidateDataSourceConfig.Response\x12i\n\x14UpgradeResourceState\x12\'.tfplugin5.UpgradeResourceState.Request\x1a(.tfplugin5.UpgradeResourceState.Response\x12H\n\tConfigure\x12\x1c.tfplugin5.Configure.Request\x1a\x1d.tfplugin5.Configure.Response\x12Q\n\x0cReadResource\x12\x1f.tfplugin5.ReadResource.Request\x1a .tfplugin5.ReadResource.Response\x12\x63\n\x12PlanResourceChange\x12%.tfplugin5.PlanResourceChange.Request\x1a&.tfplugin5.PlanResourceChange.Response\x12\x66\n\x13\x41pplyResourceChange\x12&.tfplugin5.ApplyResourceChange.Request\x1a\'.tfplugin5.ApplyResourceChange.Response\x12\x66\n\x13ImportResourceState\x12&.tfplugin5.ImportResourceState.Request\x1a\'.tfplugin5.ImportResourceState.Response\x12W\n\x0eReadDataSource\x12!.tfplugin5.ReadDataSource.Request\x1a\".tfplugin5.ReadDataSource.Response\x12Q\n\x0cGetFunctions\x12\x1f.tfplugin5.GetFunctions.Request\x1a .tfplugin5.GetFunctions.Response\x12Q\n\x0c\x43\x61llFunction\x12\x1f.tfplugin5.CallFunction.Request\x1a .tfplugin5.CallFunction.Response\x12\x39\n\x04Stop\x12\x17.tfplugin5.Stop.Request\x1a\x18.tfplugin5.Stop.Response2\x86\x03\n\x0bProvisioner\x12^\n\tGetSchema\x12\'.tfplugin5.GetProvisionerSchema.Request\x1a(.tfplugin5.GetProvisionerSchema.Response\x12x\n\x19ValidateProvisionerConfig\x12,.tfplugin5.ValidateProvisionerConfig.Request\x1a-.tfplugin5.ValidateProvisionerConfig.Response\x12\x62\n\x11ProvisionResource\x12$.tfplugin5.ProvisionResource.Request\x1a%.tfplugin5.ProvisionResource.Response0\x01\x12\x39\n\x04Stop\x12\x17.tfplugin5.Stop.Request\x1a\x18.tfplugin5.Stop.ResponseB3Z1github.com/hashicorp/terraform/internal/tfplugin5b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tfplugin5_5_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z1github.com/hashicorp/terraform/internal/tfplugin5'
  _RAWSTATE_FLATMAPENTRY._options = None
  _RAWSTATE_FLATMAPENTRY._serialized_options = b'8\001'
  _GETPROVIDERSCHEMA_RESPONSE_RESOURCESCHEMASENTRY._options = None
  _GETPROVIDERSCHEMA_RESPONSE_RESOURCESCHEMASENTRY._serialized_options = b'8\001'
  _GETPROVIDERSCHEMA_RESPONSE_DATASOURCESCHEMASENTRY._options = None
  _GETPROVIDERSCHEMA_RESPONSE_DATASOURCESCHEMASENTRY._serialized_options = b'8\001'
  _GETPROVIDERSCHEMA_RESPONSE_FUNCTIONSENTRY._options = None
  _GETPROVIDERSCHEMA_RESPONSE_FUNCTIONSENTRY._serialized_options = b'8\001'
  _GETFUNCTIONS_RESPONSE_FUNCTIONSENTRY._options = None
  _GETFUNCTIONS_RESPONSE_FUNCTIONSENTRY._serialized_options = b'8\001'
  _globals['_STRINGKIND']._serialized_start=6532
  _globals['_STRINGKIND']._serialized_end=6569
  _globals['_DYNAMICVALUE']._serialized_start=32
  _globals['_DYNAMICVALUE']._serialized_end=77
  _globals['_DIAGNOSTIC']._serialized_start=80
  _globals['_DIAGNOSTIC']._serialized_end=323
  _globals['_DIAGNOSTIC_SEVERITY']._serialized_start=254
  _globals['_DIAGNOSTIC_SEVERITY']._serialized_end=301
  _globals['_ATTRIBUTEPATH']._serialized_start=326
  _globals['_ATTRIBUTEPATH']._serialized_end=490
  _globals['_ATTRIBUTEPATH_STEP']._serialized_start=389
  _globals['_ATTRIBUTEPATH_STEP']._serialized_end=490
  _globals['_STOP']._serialized_start=492
  _globals['_STOP']._serialized_end=536
  _globals['_STOP_REQUEST']._serialized_start=500
  _globals['_STOP_REQUEST']._serialized_end=509
  _globals['_STOP_RESPONSE']._serialized_start=511
  _globals['_STOP_RESPONSE']._serialized_end=536
  _globals['_RAWSTATE']._serialized_start=538
  _globals['_RAWSTATE']._serialized_end=661
  _globals['_RAWSTATE_FLATMAPENTRY']._serialized_start=615
  _globals['_RAWSTATE_FLATMAPENTRY']._serialized_end=661
  _globals['_SCHEMA']._serialized_start=664
  _globals['_SCHEMA']._serialized_end=1404
  _globals['_SCHEMA_BLOCK']._serialized_start=732
  _globals['_SCHEMA_BLOCK']._serialized_end=947
  _globals['_SCHEMA_ATTRIBUTE']._serialized_start=950
  _globals['_SCHEMA_ATTRIBUTE']._serialized_end=1152
  _globals['_SCHEMA_NESTEDBLOCK']._serialized_start=1155
  _globals['_SCHEMA_NESTEDBLOCK']._serialized_end=1404
  _globals['_SCHEMA_NESTEDBLOCK_NESTINGMODE']._serialized_start=1327
  _globals['_SCHEMA_NESTEDBLOCK_NESTINGMODE']._serialized_end=1404
  _globals['_SERVERCAPABILITIES']._serialized_start=1406
  _globals['_SERVERCAPABILITIES']._serialized_end=1486
  _globals['_FUNCTION']._serialized_start=1489
  _globals['_FUNCTION']._serialized_end=1961
  _globals['_FUNCTION_PARAMETER']._serialized_start=1772
  _globals['_FUNCTION_PARAMETER']._serialized_end=1937
  _globals['_FUNCTION_RETURN']._serialized_start=1939
  _globals['_FUNCTION_RETURN']._serialized_end=1961
  _globals['_GETMETADATA']._serialized_start=1964
  _globals['_GETMETADATA']._serialized_end=2404
  _globals['_GETMETADATA_REQUEST']._serialized_start=500
  _globals['_GETMETADATA_REQUEST']._serialized_end=509
  _globals['_GETMETADATA_RESPONSE']._serialized_start=1991
  _globals['_GETMETADATA_RESPONSE']._serialized_end=2290
  _globals['_GETMETADATA_FUNCTIONMETADATA']._serialized_start=2292
  _globals['_GETMETADATA_FUNCTIONMETADATA']._serialized_end=2324
  _globals['_GETMETADATA_DATASOURCEMETADATA']._serialized_start=2326
  _globals['_GETMETADATA_DATASOURCEMETADATA']._serialized_end=2365
  _globals['_GETMETADATA_RESOURCEMETADATA']._serialized_start=2367
  _globals['_GETMETADATA_RESOURCEMETADATA']._serialized_end=2404
  _globals['_GETPROVIDERSCHEMA']._serialized_start=2407
  _globals['_GETPROVIDERSCHEMA']._serialized_end=3106
  _globals['_GETPROVIDERSCHEMA_REQUEST']._serialized_start=500
  _globals['_GETPROVIDERSCHEMA_REQUEST']._serialized_end=509
  _globals['_GETPROVIDERSCHEMA_RESPONSE']._serialized_start=2440
  _globals['_GETPROVIDERSCHEMA_RESPONSE']._serialized_end=3106
  _globals['_GETPROVIDERSCHEMA_RESPONSE_RESOURCESCHEMASENTRY']._serialized_start=2885
  _globals['_GETPROVIDERSCHEMA_RESPONSE_RESOURCESCHEMASENTRY']._serialized_end=2958
  _globals['_GETPROVIDERSCHEMA_RESPONSE_DATASOURCESCHEMASENTRY']._serialized_start=2960
  _globals['_GETPROVIDERSCHEMA_RESPONSE_DATASOURCESCHEMASENTRY']._serialized_end=3035
  _globals['_GETPROVIDERSCHEMA_RESPONSE_FUNCTIONSENTRY']._serialized_start=3037
  _globals['_GETPROVIDERSCHEMA_RESPONSE_FUNCTIONSENTRY']._serialized_end=3106
  _globals['_PREPAREPROVIDERCONFIG']._serialized_start=3109
  _globals['_PREPAREPROVIDERCONFIG']._serialized_end=3290
  _globals['_PREPAREPROVIDERCONFIG_REQUEST']._serialized_start=3134
  _globals['_PREPAREPROVIDERCONFIG_REQUEST']._serialized_end=3184
  _globals['_PREPAREPROVIDERCONFIG_RESPONSE']._serialized_start=3186
  _globals['_PREPAREPROVIDERCONFIG_RESPONSE']._serialized_end=3290
  _globals['_UPGRADERESOURCESTATE']._serialized_start=3293
  _globals['_UPGRADERESOURCESTATE']._serialized_end=3507
  _globals['_UPGRADERESOURCESTATE_REQUEST']._serialized_start=3317
  _globals['_UPGRADERESOURCESTATE_REQUEST']._serialized_end=3402
  _globals['_UPGRADERESOURCESTATE_RESPONSE']._serialized_start=3404
  _globals['_UPGRADERESOURCESTATE_RESPONSE']._serialized_end=3507
  _globals['_VALIDATERESOURCETYPECONFIG']._serialized_start=3510
  _globals['_VALIDATERESOURCETYPECONFIG']._serialized_end=3665
  _globals['_VALIDATERESOURCETYPECONFIG_REQUEST']._serialized_start=3540
  _globals['_VALIDATERESOURCETYPECONFIG_REQUEST']._serialized_end=3609
  _globals['_VALIDATERESOURCETYPECONFIG_RESPONSE']._serialized_start=3611
  _globals['_VALIDATERESOURCETYPECONFIG_RESPONSE']._serialized_end=3665
  _globals['_VALIDATEDATASOURCECONFIG']._serialized_start=3668
  _globals['_VALIDATEDATASOURCECONFIG']._serialized_end=3821
  _globals['_VALIDATEDATASOURCECONFIG_REQUEST']._serialized_start=3540
  _globals['_VALIDATEDATASOURCECONFIG_REQUEST']._serialized_end=3609
  _globals['_VALIDATEDATASOURCECONFIG_RESPONSE']._serialized_start=3611
  _globals['_VALIDATEDATASOURCECONFIG_RESPONSE']._serialized_end=3665
  _globals['_CONFIGURE']._serialized_start=3824
  _globals['_CONFIGURE']._serialized_end=3970
  _globals['_CONFIGURE_REQUEST']._serialized_start=3837
  _globals['_CONFIGURE_REQUEST']._serialized_end=3914
  _globals['_CONFIGURE_RESPONSE']._serialized_start=3611
  _globals['_CONFIGURE_RESPONSE']._serialized_end=3665
  _globals['_READRESOURCE']._serialized_start=3973
  _globals['_READRESOURCE']._serialized_end=4248
  _globals['_READRESOURCE_REQUEST']._serialized_start=3990
  _globals['_READRESOURCE_REQUEST']._serialized_end=4131
  _globals['_READRESOURCE_RESPONSE']._serialized_start=4133
  _globals['_READRESOURCE_RESPONSE']._serialized_end=4248
  _globals['_PLANRESOURCECHANGE']._serialized_start=4251
  _globals['_PLANRESOURCECHANGE']._serialized_end=4723
  _globals['_PLANRESOURCECHANGE_REQUEST']._serialized_start=4274
  _globals['_PLANRESOURCECHANGE_REQUEST']._serialized_end=4513
  _globals['_PLANRESOURCECHANGE_RESPONSE']._serialized_start=4516
  _globals['_PLANRESOURCECHANGE_RESPONSE']._serialized_end=4723
  _globals['_APPLYRESOURCECHANGE']._serialized_start=4726
  _globals['_APPLYRESOURCECHANGE']._serialized_end=5132
  _globals['_APPLYRESOURCECHANGE_REQUEST']._serialized_start=4750
  _globals['_APPLYRESOURCECHANGE_REQUEST']._serialized_end=4986
  _globals['_APPLYRESOURCECHANGE_RESPONSE']._serialized_start=4989
  _globals['_APPLYRESOURCECHANGE_RESPONSE']._serialized_end=5132
  _globals['_IMPORTRESOURCESTATE']._serialized_start=5135
  _globals['_IMPORTRESOURCESTATE']._serialized_end=5428
  _globals['_IMPORTRESOURCESTATE_REQUEST']._serialized_start=5158
  _globals['_IMPORTRESOURCESTATE_REQUEST']._serialized_end=5198
  _globals['_IMPORTRESOURCESTATE_IMPORTEDRESOURCE']._serialized_start=5200
  _globals['_IMPORTRESOURCESTATE_IMPORTEDRESOURCE']._serialized_end=5294
  _globals['_IMPORTRESOURCESTATE_RESPONSE']._serialized_start=5297
  _globals['_IMPORTRESOURCESTATE_RESPONSE']._serialized_end=5428
  _globals['_READDATASOURCE']._serialized_start=5431
  _globals['_READDATASOURCE']._serialized_end=5662
  _globals['_READDATASOURCE_REQUEST']._serialized_start=5449
  _globals['_READDATASOURCE_REQUEST']._serialized_end=5566
  _globals['_READDATASOURCE_RESPONSE']._serialized_start=5568
  _globals['_READDATASOURCE_RESPONSE']._serialized_end=5662
  _globals['_GETPROVISIONERSCHEMA']._serialized_start=5665
  _globals['_GETPROVISIONERSCHEMA']._serialized_end=5794
  _globals['_GETPROVISIONERSCHEMA_REQUEST']._serialized_start=500
  _globals['_GETPROVISIONERSCHEMA_REQUEST']._serialized_end=509
  _globals['_GETPROVISIONERSCHEMA_RESPONSE']._serialized_start=5700
  _globals['_GETPROVISIONERSCHEMA_RESPONSE']._serialized_end=5794
  _globals['_VALIDATEPROVISIONERCONFIG']._serialized_start=5797
  _globals['_VALIDATEPROVISIONERCONFIG']._serialized_end=5932
  _globals['_VALIDATEPROVISIONERCONFIG_REQUEST']._serialized_start=3134
  _globals['_VALIDATEPROVISIONERCONFIG_REQUEST']._serialized_end=3184
  _globals['_VALIDATEPROVISIONERCONFIG_RESPONSE']._serialized_start=3611
  _globals['_VALIDATEPROVISIONERCONFIG_RESPONSE']._serialized_end=3665
  _globals['_PROVISIONRESOURCE']._serialized_start=5935
  _globals['_PROVISIONRESOURCE']._serialized_end=6123
  _globals['_PROVISIONRESOURCE_REQUEST']._serialized_start=5956
  _globals['_PROVISIONRESOURCE_REQUEST']._serialized_end=6051
  _globals['_PROVISIONRESOURCE_RESPONSE']._serialized_start=6053
  _globals['_PROVISIONRESOURCE_RESPONSE']._serialized_end=6123
  _globals['_GETFUNCTIONS']._serialized_start=6126
  _globals['_GETFUNCTIONS']._serialized_end=6347
  _globals['_GETFUNCTIONS_REQUEST']._serialized_start=500
  _globals['_GETFUNCTIONS_REQUEST']._serialized_end=509
  _globals['_GETFUNCTIONS_RESPONSE']._serialized_start=6154
  _globals['_GETFUNCTIONS_RESPONSE']._serialized_end=6347
  _globals['_GETFUNCTIONS_RESPONSE_FUNCTIONSENTRY']._serialized_start=3037
  _globals['_GETFUNCTIONS_RESPONSE_FUNCTIONSENTRY']._serialized_end=3106
  _globals['_CALLFUNCTION']._serialized_start=6350
  _globals['_CALLFUNCTION']._serialized_end=6530
  _globals['_CALLFUNCTION_REQUEST']._serialized_start=6366
  _globals['_CALLFUNCTION_REQUEST']._serialized_end=6433
  _globals['_CALLFUNCTION_RESPONSE']._serialized_start=6435
  _globals['_CALLFUNCTION_RESPONSE']._serialized_end=6530
  _globals['_PROVIDER']._serialized_start=6572
  _globals['_PROVIDER']._serialized_end=7993
  _globals['_PROVISIONER']._serialized_start=7996
  _globals['_PROVISIONER']._serialized_end=8386
# @@protoc_insertion_point(module_scope)