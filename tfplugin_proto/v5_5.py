# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v5_5.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nv5_5.proto\x12\x02v5\"-\n\x0c\x44ynamicValue\x12\x0f\n\x07msgpack\x18\x01 \x01(\x0c\x12\x0c\n\x04json\x18\x02 \x01(\x0c\"\xe5\x01\n\nDiagnostic\x12)\n\x08severity\x18\x01 \x01(\x0e\x32\x17.v5.Diagnostic.Severity\x12\x0f\n\x07summary\x18\x02 \x01(\t\x12\x0e\n\x06\x64\x65tail\x18\x03 \x01(\t\x12$\n\tattribute\x18\x04 \x01(\x0b\x32\x11.v5.AttributePath\x12\x1e\n\x11\x66unction_argument\x18\x05 \x01(\x03H\x00\x88\x01\x01\"/\n\x08Severity\x12\x0b\n\x07INVALID\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x12\x0b\n\x07WARNING\x10\x02\x42\x14\n\x12_function_argument\"\x9d\x01\n\rAttributePath\x12%\n\x05steps\x18\x01 \x03(\x0b\x32\x16.v5.AttributePath.Step\x1a\x65\n\x04Step\x12\x18\n\x0e\x61ttribute_name\x18\x01 \x01(\tH\x00\x12\x1c\n\x12\x65lement_key_string\x18\x02 \x01(\tH\x00\x12\x19\n\x0f\x65lement_key_int\x18\x03 \x01(\x03H\x00\x42\n\n\x08selector\",\n\x04Stop\x1a\t\n\x07Request\x1a\x19\n\x08Response\x12\r\n\x05\x45rror\x18\x01 \x01(\t\"t\n\x08RawState\x12\x0c\n\x04json\x18\x01 \x01(\x0c\x12*\n\x07\x66latmap\x18\x02 \x03(\x0b\x32\x19.v5.RawState.FlatmapEntry\x1a.\n\x0c\x46latmapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xb3\x05\n\x06Schema\x12\x0f\n\x07version\x18\x01 \x01(\x03\x12\x1f\n\x05\x62lock\x18\x02 \x01(\x0b\x32\x10.v5.Schema.Block\x1a\xc2\x01\n\x05\x42lock\x12\x0f\n\x07version\x18\x01 \x01(\x03\x12(\n\nattributes\x18\x02 \x03(\x0b\x32\x14.v5.Schema.Attribute\x12+\n\x0b\x62lock_types\x18\x03 \x03(\x0b\x32\x16.v5.Schema.NestedBlock\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12(\n\x10\x64\x65scription_kind\x18\x05 \x01(\x0e\x32\x0e.v5.StringKind\x12\x12\n\ndeprecated\x18\x06 \x01(\x08\x1a\xc3\x01\n\tAttribute\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\x0c\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x10\n\x08required\x18\x04 \x01(\x08\x12\x10\n\x08optional\x18\x05 \x01(\x08\x12\x10\n\x08\x63omputed\x18\x06 \x01(\x08\x12\x11\n\tsensitive\x18\x07 \x01(\x08\x12(\n\x10\x64\x65scription_kind\x18\x08 \x01(\x0e\x32\x0e.v5.StringKind\x12\x12\n\ndeprecated\x18\t \x01(\x08\x1a\xeb\x01\n\x0bNestedBlock\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\x1f\n\x05\x62lock\x18\x02 \x01(\x0b\x32\x10.v5.Schema.Block\x12\x33\n\x07nesting\x18\x03 \x01(\x0e\x32\".v5.Schema.NestedBlock.NestingMode\x12\x11\n\tmin_items\x18\x04 \x01(\x03\x12\x11\n\tmax_items\x18\x05 \x01(\x03\"M\n\x0bNestingMode\x12\x0b\n\x07INVALID\x10\x00\x12\n\n\x06SINGLE\x10\x01\x12\x08\n\x04LIST\x10\x02\x12\x07\n\x03SET\x10\x03\x12\x07\n\x03MAP\x10\x04\x12\t\n\x05GROUP\x10\x05\"P\n\x12ServerCapabilities\x12\x14\n\x0cplan_destroy\x18\x01 \x01(\x08\x12$\n\x1cget_provider_schema_optional\x18\x02 \x01(\x08\"\xb5\x03\n\x08\x46unction\x12*\n\nparameters\x18\x01 \x03(\x0b\x32\x16.v5.Function.Parameter\x12\x32\n\x12variadic_parameter\x18\x02 \x01(\x0b\x32\x16.v5.Function.Parameter\x12#\n\x06return\x18\x03 \x01(\x0b\x32\x13.v5.Function.Return\x12\x0f\n\x07summary\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12(\n\x10\x64\x65scription_kind\x18\x06 \x01(\x0e\x32\x0e.v5.StringKind\x12\x1b\n\x13\x64\x65precation_message\x18\x07 \x01(\t\x1a\x9e\x01\n\tParameter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\x0c\x12\x18\n\x10\x61llow_null_value\x18\x03 \x01(\x08\x12\x1c\n\x14\x61llow_unknown_values\x18\x04 \x01(\x08\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12(\n\x10\x64\x65scription_kind\x18\x06 \x01(\x0e\x32\x0e.v5.StringKind\x1a\x16\n\x06Return\x12\x0c\n\x04type\x18\x01 \x01(\x0c\"\x95\x03\n\x0bGetMetadata\x1a\t\n\x07Request\x1a\x88\x02\n\x08Response\x12\x33\n\x13server_capabilities\x18\x01 \x01(\x0b\x32\x16.v5.ServerCapabilities\x12#\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x0e.v5.Diagnostic\x12\x38\n\x0c\x64\x61ta_sources\x18\x03 \x03(\x0b\x32\".v5.GetMetadata.DataSourceMetadata\x12\x33\n\tresources\x18\x04 \x03(\x0b\x32 .v5.GetMetadata.ResourceMetadata\x12\x33\n\tfunctions\x18\x05 \x03(\x0b\x32 .v5.GetMetadata.FunctionMetadata\x1a \n\x10\x46unctionMetadata\x12\x0c\n\x04name\x18\x01 \x01(\t\x1a\'\n\x12\x44\x61taSourceMetadata\x12\x11\n\ttype_name\x18\x01 \x01(\t\x1a%\n\x10ResourceMetadata\x12\x11\n\ttype_name\x18\x01 \x01(\t\"\xf5\x04\n\x11GetProviderSchema\x1a\t\n\x07Request\x1a\xd4\x04\n\x08Response\x12\x1c\n\x08provider\x18\x01 \x01(\x0b\x32\n.v5.Schema\x12M\n\x10resource_schemas\x18\x02 \x03(\x0b\x32\x33.v5.GetProviderSchema.Response.ResourceSchemasEntry\x12R\n\x13\x64\x61ta_source_schemas\x18\x03 \x03(\x0b\x32\x35.v5.GetProviderSchema.Response.DataSourceSchemasEntry\x12@\n\tfunctions\x18\x07 \x03(\x0b\x32-.v5.GetProviderSchema.Response.FunctionsEntry\x12#\n\x0b\x64iagnostics\x18\x04 \x03(\x0b\x32\x0e.v5.Diagnostic\x12!\n\rprovider_meta\x18\x05 \x01(\x0b\x32\n.v5.Schema\x12\x33\n\x13server_capabilities\x18\x06 \x01(\x0b\x32\x16.v5.ServerCapabilities\x1a\x42\n\x14ResourceSchemasEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x19\n\x05value\x18\x02 \x01(\x0b\x32\n.v5.Schema:\x02\x38\x01\x1a\x44\n\x16\x44\x61taSourceSchemasEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x19\n\x05value\x18\x02 \x01(\x0b\x32\n.v5.Schema:\x02\x38\x01\x1a>\n\x0e\x46unctionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1b\n\x05value\x18\x02 \x01(\x0b\x32\x0c.v5.Function:\x02\x38\x01\"\xa0\x01\n\x15PrepareProviderConfig\x1a+\n\x07Request\x12 \n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x10.v5.DynamicValue\x1aZ\n\x08Response\x12)\n\x0fprepared_config\x18\x01 \x01(\x0b\x32\x10.v5.DynamicValue\x12#\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x0e.v5.Diagnostic\"\xc1\x01\n\x14UpgradeResourceState\x1aN\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x03\x12\x1f\n\traw_state\x18\x03 \x01(\x0b\x32\x0c.v5.RawState\x1aY\n\x08Response\x12(\n\x0eupgraded_state\x18\x01 \x01(\x0b\x32\x10.v5.DynamicValue\x12#\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x0e.v5.Diagnostic\"\x8d\x01\n\x1aValidateResourceTypeConfig\x1a>\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12 \n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x10.v5.DynamicValue\x1a/\n\x08Response\x12#\n\x0b\x64iagnostics\x18\x01 \x03(\x0b\x32\x0e.v5.Diagnostic\"\x8b\x01\n\x18ValidateDataSourceConfig\x1a>\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12 \n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x10.v5.DynamicValue\x1a/\n\x08Response\x12#\n\x0b\x64iagnostics\x18\x01 \x03(\x0b\x32\x0e.v5.Diagnostic\"\x84\x01\n\tConfigure\x1a\x46\n\x07Request\x12\x19\n\x11terraform_version\x18\x01 \x01(\t\x12 \n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x10.v5.DynamicValue\x1a/\n\x08Response\x12#\n\x0b\x64iagnostics\x18\x01 \x03(\x0b\x32\x0e.v5.Diagnostic\"\xf6\x01\n\x0cReadResource\x1a\x7f\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\'\n\rcurrent_state\x18\x02 \x01(\x0b\x32\x10.v5.DynamicValue\x12\x0f\n\x07private\x18\x03 \x01(\x0c\x12\'\n\rprovider_meta\x18\x04 \x01(\x0b\x32\x10.v5.DynamicValue\x1a\x65\n\x08Response\x12#\n\tnew_state\x18\x01 \x01(\x0b\x32\x10.v5.DynamicValue\x12#\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x0e.v5.Diagnostic\x12\x0f\n\x07private\x18\x03 \x01(\x0c\"\xa7\x03\n\x12PlanResourceChange\x1a\xd3\x01\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12%\n\x0bprior_state\x18\x02 \x01(\x0b\x32\x10.v5.DynamicValue\x12,\n\x12proposed_new_state\x18\x03 \x01(\x0b\x32\x10.v5.DynamicValue\x12 \n\x06\x63onfig\x18\x04 \x01(\x0b\x32\x10.v5.DynamicValue\x12\x15\n\rprior_private\x18\x05 \x01(\x0c\x12\'\n\rprovider_meta\x18\x06 \x01(\x0b\x32\x10.v5.DynamicValue\x1a\xba\x01\n\x08Response\x12\'\n\rplanned_state\x18\x01 \x01(\x0b\x32\x10.v5.DynamicValue\x12+\n\x10requires_replace\x18\x02 \x03(\x0b\x32\x11.v5.AttributePath\x12\x17\n\x0fplanned_private\x18\x03 \x01(\x0c\x12#\n\x0b\x64iagnostics\x18\x04 \x03(\x0b\x32\x0e.v5.Diagnostic\x12\x1a\n\x12legacy_type_system\x18\x05 \x01(\x08\"\xec\x02\n\x13\x41pplyResourceChange\x1a\xd0\x01\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12%\n\x0bprior_state\x18\x02 \x01(\x0b\x32\x10.v5.DynamicValue\x12\'\n\rplanned_state\x18\x03 \x01(\x0b\x32\x10.v5.DynamicValue\x12 \n\x06\x63onfig\x18\x04 \x01(\x0b\x32\x10.v5.DynamicValue\x12\x17\n\x0fplanned_private\x18\x05 \x01(\x0c\x12\'\n\rprovider_meta\x18\x06 \x01(\x0b\x32\x10.v5.DynamicValue\x1a\x81\x01\n\x08Response\x12#\n\tnew_state\x18\x01 \x01(\x0b\x32\x10.v5.DynamicValue\x12\x0f\n\x07private\x18\x02 \x01(\x0c\x12#\n\x0b\x64iagnostics\x18\x03 \x03(\x0b\x32\x0e.v5.Diagnostic\x12\x1a\n\x12legacy_type_system\x18\x04 \x01(\x08\"\x8f\x02\n\x13ImportResourceState\x1a(\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x1aW\n\x10ImportedResource\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\x1f\n\x05state\x18\x02 \x01(\x0b\x32\x10.v5.DynamicValue\x12\x0f\n\x07private\x18\x03 \x01(\x0c\x1au\n\x08Response\x12\x44\n\x12imported_resources\x18\x01 \x03(\x0b\x32(.v5.ImportResourceState.ImportedResource\x12#\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x0e.v5.Diagnostic\"\xcb\x01\n\x0eReadDataSource\x1ag\n\x07Request\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12 \n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x10.v5.DynamicValue\x12\'\n\rprovider_meta\x18\x03 \x01(\x0b\x32\x10.v5.DynamicValue\x1aP\n\x08Response\x12\x1f\n\x05state\x18\x01 \x01(\x0b\x32\x10.v5.DynamicValue\x12#\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x0e.v5.Diagnostic\"s\n\x14GetProvisionerSchema\x1a\t\n\x07Request\x1aP\n\x08Response\x12\x1f\n\x0bprovisioner\x18\x01 \x01(\x0b\x32\n.v5.Schema\x12#\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x0e.v5.Diagnostic\"y\n\x19ValidateProvisionerConfig\x1a+\n\x07Request\x12 \n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x10.v5.DynamicValue\x1a/\n\x08Response\x12#\n\x0b\x64iagnostics\x18\x01 \x03(\x0b\x32\x0e.v5.Diagnostic\"\xa7\x01\n\x11ProvisionResource\x1aQ\n\x07Request\x12 \n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x10.v5.DynamicValue\x12$\n\nconnection\x18\x02 \x01(\x0b\x32\x10.v5.DynamicValue\x1a?\n\x08Response\x12\x0e\n\x06output\x18\x01 \x01(\t\x12#\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x0e.v5.Diagnostic\"\xc8\x01\n\x0cGetFunctions\x1a\t\n\x07Request\x1a\xac\x01\n\x08Response\x12;\n\tfunctions\x18\x01 \x03(\x0b\x32(.v5.GetFunctions.Response.FunctionsEntry\x12#\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x0e.v5.Diagnostic\x1a>\n\x0e\x46unctionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1b\n\x05value\x18\x02 \x01(\x0b\x32\x0c.v5.Function:\x02\x38\x01\"\x9f\x01\n\x0c\x43\x61llFunction\x1a<\n\x07Request\x12\x0c\n\x04name\x18\x01 \x01(\t\x12#\n\targuments\x18\x02 \x03(\x0b\x32\x10.v5.DynamicValue\x1aQ\n\x08Response\x12 \n\x06result\x18\x01 \x01(\x0b\x32\x10.v5.DynamicValue\x12#\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x0e.v5.Diagnostic*%\n\nStringKind\x12\t\n\x05PLAIN\x10\x00\x12\x0c\n\x08MARKDOWN\x10\x01\x32\xbb\t\n\x08Provider\x12@\n\x0bGetMetadata\x12\x17.v5.GetMetadata.Request\x1a\x18.v5.GetMetadata.Response\x12J\n\tGetSchema\x12\x1d.v5.GetProviderSchema.Request\x1a\x1e.v5.GetProviderSchema.Response\x12^\n\x15PrepareProviderConfig\x12!.v5.PrepareProviderConfig.Request\x1a\".v5.PrepareProviderConfig.Response\x12m\n\x1aValidateResourceTypeConfig\x12&.v5.ValidateResourceTypeConfig.Request\x1a\'.v5.ValidateResourceTypeConfig.Response\x12g\n\x18ValidateDataSourceConfig\x12$.v5.ValidateDataSourceConfig.Request\x1a%.v5.ValidateDataSourceConfig.Response\x12[\n\x14UpgradeResourceState\x12 .v5.UpgradeResourceState.Request\x1a!.v5.UpgradeResourceState.Response\x12:\n\tConfigure\x12\x15.v5.Configure.Request\x1a\x16.v5.Configure.Response\x12\x43\n\x0cReadResource\x12\x18.v5.ReadResource.Request\x1a\x19.v5.ReadResource.Response\x12U\n\x12PlanResourceChange\x12\x1e.v5.PlanResourceChange.Request\x1a\x1f.v5.PlanResourceChange.Response\x12X\n\x13\x41pplyResourceChange\x12\x1f.v5.ApplyResourceChange.Request\x1a .v5.ApplyResourceChange.Response\x12X\n\x13ImportResourceState\x12\x1f.v5.ImportResourceState.Request\x1a .v5.ImportResourceState.Response\x12I\n\x0eReadDataSource\x12\x1a.v5.ReadDataSource.Request\x1a\x1b.v5.ReadDataSource.Response\x12\x43\n\x0cGetFunctions\x12\x18.v5.GetFunctions.Request\x1a\x19.v5.GetFunctions.Response\x12\x43\n\x0c\x43\x61llFunction\x12\x18.v5.CallFunction.Request\x1a\x19.v5.CallFunction.Response\x12+\n\x04Stop\x12\x10.v5.Stop.Request\x1a\x11.v5.Stop.Response2\xce\x02\n\x0bProvisioner\x12P\n\tGetSchema\x12 .v5.GetProvisionerSchema.Request\x1a!.v5.GetProvisionerSchema.Response\x12j\n\x19ValidateProvisionerConfig\x12%.v5.ValidateProvisionerConfig.Request\x1a&.v5.ValidateProvisionerConfig.Response\x12T\n\x11ProvisionResource\x12\x1d.v5.ProvisionResource.Request\x1a\x1e.v5.ProvisionResource.Response0\x01\x12+\n\x04Stop\x12\x10.v5.Stop.Request\x1a\x11.v5.Stop.ResponseB3Z1github.com/hashicorp/terraform/internal/tfplugin5b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'v5_5_pb2', _globals)
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
  _globals['_STRINGKIND']._serialized_start=5954
  _globals['_STRINGKIND']._serialized_end=5991
  _globals['_DYNAMICVALUE']._serialized_start=18
  _globals['_DYNAMICVALUE']._serialized_end=63
  _globals['_DIAGNOSTIC']._serialized_start=66
  _globals['_DIAGNOSTIC']._serialized_end=295
  _globals['_DIAGNOSTIC_SEVERITY']._serialized_start=226
  _globals['_DIAGNOSTIC_SEVERITY']._serialized_end=273
  _globals['_ATTRIBUTEPATH']._serialized_start=298
  _globals['_ATTRIBUTEPATH']._serialized_end=455
  _globals['_ATTRIBUTEPATH_STEP']._serialized_start=354
  _globals['_ATTRIBUTEPATH_STEP']._serialized_end=455
  _globals['_STOP']._serialized_start=457
  _globals['_STOP']._serialized_end=501
  _globals['_STOP_REQUEST']._serialized_start=465
  _globals['_STOP_REQUEST']._serialized_end=474
  _globals['_STOP_RESPONSE']._serialized_start=476
  _globals['_STOP_RESPONSE']._serialized_end=501
  _globals['_RAWSTATE']._serialized_start=503
  _globals['_RAWSTATE']._serialized_end=619
  _globals['_RAWSTATE_FLATMAPENTRY']._serialized_start=573
  _globals['_RAWSTATE_FLATMAPENTRY']._serialized_end=619
  _globals['_SCHEMA']._serialized_start=622
  _globals['_SCHEMA']._serialized_end=1313
  _globals['_SCHEMA_BLOCK']._serialized_start=683
  _globals['_SCHEMA_BLOCK']._serialized_end=877
  _globals['_SCHEMA_ATTRIBUTE']._serialized_start=880
  _globals['_SCHEMA_ATTRIBUTE']._serialized_end=1075
  _globals['_SCHEMA_NESTEDBLOCK']._serialized_start=1078
  _globals['_SCHEMA_NESTEDBLOCK']._serialized_end=1313
  _globals['_SCHEMA_NESTEDBLOCK_NESTINGMODE']._serialized_start=1236
  _globals['_SCHEMA_NESTEDBLOCK_NESTINGMODE']._serialized_end=1313
  _globals['_SERVERCAPABILITIES']._serialized_start=1315
  _globals['_SERVERCAPABILITIES']._serialized_end=1395
  _globals['_FUNCTION']._serialized_start=1398
  _globals['_FUNCTION']._serialized_end=1835
  _globals['_FUNCTION_PARAMETER']._serialized_start=1653
  _globals['_FUNCTION_PARAMETER']._serialized_end=1811
  _globals['_FUNCTION_RETURN']._serialized_start=1813
  _globals['_FUNCTION_RETURN']._serialized_end=1835
  _globals['_GETMETADATA']._serialized_start=1838
  _globals['_GETMETADATA']._serialized_end=2243
  _globals['_GETMETADATA_REQUEST']._serialized_start=465
  _globals['_GETMETADATA_REQUEST']._serialized_end=474
  _globals['_GETMETADATA_RESPONSE']._serialized_start=1865
  _globals['_GETMETADATA_RESPONSE']._serialized_end=2129
  _globals['_GETMETADATA_FUNCTIONMETADATA']._serialized_start=2131
  _globals['_GETMETADATA_FUNCTIONMETADATA']._serialized_end=2163
  _globals['_GETMETADATA_DATASOURCEMETADATA']._serialized_start=2165
  _globals['_GETMETADATA_DATASOURCEMETADATA']._serialized_end=2204
  _globals['_GETMETADATA_RESOURCEMETADATA']._serialized_start=2206
  _globals['_GETMETADATA_RESOURCEMETADATA']._serialized_end=2243
  _globals['_GETPROVIDERSCHEMA']._serialized_start=2246
  _globals['_GETPROVIDERSCHEMA']._serialized_end=2875
  _globals['_GETPROVIDERSCHEMA_REQUEST']._serialized_start=465
  _globals['_GETPROVIDERSCHEMA_REQUEST']._serialized_end=474
  _globals['_GETPROVIDERSCHEMA_RESPONSE']._serialized_start=2279
  _globals['_GETPROVIDERSCHEMA_RESPONSE']._serialized_end=2875
  _globals['_GETPROVIDERSCHEMA_RESPONSE_RESOURCESCHEMASENTRY']._serialized_start=2675
  _globals['_GETPROVIDERSCHEMA_RESPONSE_RESOURCESCHEMASENTRY']._serialized_end=2741
  _globals['_GETPROVIDERSCHEMA_RESPONSE_DATASOURCESCHEMASENTRY']._serialized_start=2743
  _globals['_GETPROVIDERSCHEMA_RESPONSE_DATASOURCESCHEMASENTRY']._serialized_end=2811
  _globals['_GETPROVIDERSCHEMA_RESPONSE_FUNCTIONSENTRY']._serialized_start=2813
  _globals['_GETPROVIDERSCHEMA_RESPONSE_FUNCTIONSENTRY']._serialized_end=2875
  _globals['_PREPAREPROVIDERCONFIG']._serialized_start=2878
  _globals['_PREPAREPROVIDERCONFIG']._serialized_end=3038
  _globals['_PREPAREPROVIDERCONFIG_REQUEST']._serialized_start=2903
  _globals['_PREPAREPROVIDERCONFIG_REQUEST']._serialized_end=2946
  _globals['_PREPAREPROVIDERCONFIG_RESPONSE']._serialized_start=2948
  _globals['_PREPAREPROVIDERCONFIG_RESPONSE']._serialized_end=3038
  _globals['_UPGRADERESOURCESTATE']._serialized_start=3041
  _globals['_UPGRADERESOURCESTATE']._serialized_end=3234
  _globals['_UPGRADERESOURCESTATE_REQUEST']._serialized_start=3065
  _globals['_UPGRADERESOURCESTATE_REQUEST']._serialized_end=3143
  _globals['_UPGRADERESOURCESTATE_RESPONSE']._serialized_start=3145
  _globals['_UPGRADERESOURCESTATE_RESPONSE']._serialized_end=3234
  _globals['_VALIDATERESOURCETYPECONFIG']._serialized_start=3237
  _globals['_VALIDATERESOURCETYPECONFIG']._serialized_end=3378
  _globals['_VALIDATERESOURCETYPECONFIG_REQUEST']._serialized_start=3267
  _globals['_VALIDATERESOURCETYPECONFIG_REQUEST']._serialized_end=3329
  _globals['_VALIDATERESOURCETYPECONFIG_RESPONSE']._serialized_start=3331
  _globals['_VALIDATERESOURCETYPECONFIG_RESPONSE']._serialized_end=3378
  _globals['_VALIDATEDATASOURCECONFIG']._serialized_start=3381
  _globals['_VALIDATEDATASOURCECONFIG']._serialized_end=3520
  _globals['_VALIDATEDATASOURCECONFIG_REQUEST']._serialized_start=3267
  _globals['_VALIDATEDATASOURCECONFIG_REQUEST']._serialized_end=3329
  _globals['_VALIDATEDATASOURCECONFIG_RESPONSE']._serialized_start=3331
  _globals['_VALIDATEDATASOURCECONFIG_RESPONSE']._serialized_end=3378
  _globals['_CONFIGURE']._serialized_start=3523
  _globals['_CONFIGURE']._serialized_end=3655
  _globals['_CONFIGURE_REQUEST']._serialized_start=3536
  _globals['_CONFIGURE_REQUEST']._serialized_end=3606
  _globals['_CONFIGURE_RESPONSE']._serialized_start=3331
  _globals['_CONFIGURE_RESPONSE']._serialized_end=3378
  _globals['_READRESOURCE']._serialized_start=3658
  _globals['_READRESOURCE']._serialized_end=3904
  _globals['_READRESOURCE_REQUEST']._serialized_start=3674
  _globals['_READRESOURCE_REQUEST']._serialized_end=3801
  _globals['_READRESOURCE_RESPONSE']._serialized_start=3803
  _globals['_READRESOURCE_RESPONSE']._serialized_end=3904
  _globals['_PLANRESOURCECHANGE']._serialized_start=3907
  _globals['_PLANRESOURCECHANGE']._serialized_end=4330
  _globals['_PLANRESOURCECHANGE_REQUEST']._serialized_start=3930
  _globals['_PLANRESOURCECHANGE_REQUEST']._serialized_end=4141
  _globals['_PLANRESOURCECHANGE_RESPONSE']._serialized_start=4144
  _globals['_PLANRESOURCECHANGE_RESPONSE']._serialized_end=4330
  _globals['_APPLYRESOURCECHANGE']._serialized_start=4333
  _globals['_APPLYRESOURCECHANGE']._serialized_end=4697
  _globals['_APPLYRESOURCECHANGE_REQUEST']._serialized_start=4357
  _globals['_APPLYRESOURCECHANGE_REQUEST']._serialized_end=4565
  _globals['_APPLYRESOURCECHANGE_RESPONSE']._serialized_start=4568
  _globals['_APPLYRESOURCECHANGE_RESPONSE']._serialized_end=4697
  _globals['_IMPORTRESOURCESTATE']._serialized_start=4700
  _globals['_IMPORTRESOURCESTATE']._serialized_end=4971
  _globals['_IMPORTRESOURCESTATE_REQUEST']._serialized_start=4723
  _globals['_IMPORTRESOURCESTATE_REQUEST']._serialized_end=4763
  _globals['_IMPORTRESOURCESTATE_IMPORTEDRESOURCE']._serialized_start=4765
  _globals['_IMPORTRESOURCESTATE_IMPORTEDRESOURCE']._serialized_end=4852
  _globals['_IMPORTRESOURCESTATE_RESPONSE']._serialized_start=4854
  _globals['_IMPORTRESOURCESTATE_RESPONSE']._serialized_end=4971
  _globals['_READDATASOURCE']._serialized_start=4974
  _globals['_READDATASOURCE']._serialized_end=5177
  _globals['_READDATASOURCE_REQUEST']._serialized_start=4992
  _globals['_READDATASOURCE_REQUEST']._serialized_end=5095
  _globals['_READDATASOURCE_RESPONSE']._serialized_start=5097
  _globals['_READDATASOURCE_RESPONSE']._serialized_end=5177
  _globals['_GETPROVISIONERSCHEMA']._serialized_start=5179
  _globals['_GETPROVISIONERSCHEMA']._serialized_end=5294
  _globals['_GETPROVISIONERSCHEMA_REQUEST']._serialized_start=465
  _globals['_GETPROVISIONERSCHEMA_REQUEST']._serialized_end=474
  _globals['_GETPROVISIONERSCHEMA_RESPONSE']._serialized_start=5214
  _globals['_GETPROVISIONERSCHEMA_RESPONSE']._serialized_end=5294
  _globals['_VALIDATEPROVISIONERCONFIG']._serialized_start=5296
  _globals['_VALIDATEPROVISIONERCONFIG']._serialized_end=5417
  _globals['_VALIDATEPROVISIONERCONFIG_REQUEST']._serialized_start=2903
  _globals['_VALIDATEPROVISIONERCONFIG_REQUEST']._serialized_end=2946
  _globals['_VALIDATEPROVISIONERCONFIG_RESPONSE']._serialized_start=3331
  _globals['_VALIDATEPROVISIONERCONFIG_RESPONSE']._serialized_end=3378
  _globals['_PROVISIONRESOURCE']._serialized_start=5420
  _globals['_PROVISIONRESOURCE']._serialized_end=5587
  _globals['_PROVISIONRESOURCE_REQUEST']._serialized_start=5441
  _globals['_PROVISIONRESOURCE_REQUEST']._serialized_end=5522
  _globals['_PROVISIONRESOURCE_RESPONSE']._serialized_start=5524
  _globals['_PROVISIONRESOURCE_RESPONSE']._serialized_end=5587
  _globals['_GETFUNCTIONS']._serialized_start=5590
  _globals['_GETFUNCTIONS']._serialized_end=5790
  _globals['_GETFUNCTIONS_REQUEST']._serialized_start=465
  _globals['_GETFUNCTIONS_REQUEST']._serialized_end=474
  _globals['_GETFUNCTIONS_RESPONSE']._serialized_start=5618
  _globals['_GETFUNCTIONS_RESPONSE']._serialized_end=5790
  _globals['_GETFUNCTIONS_RESPONSE_FUNCTIONSENTRY']._serialized_start=2813
  _globals['_GETFUNCTIONS_RESPONSE_FUNCTIONSENTRY']._serialized_end=2875
  _globals['_CALLFUNCTION']._serialized_start=5793
  _globals['_CALLFUNCTION']._serialized_end=5952
  _globals['_CALLFUNCTION_REQUEST']._serialized_start=5809
  _globals['_CALLFUNCTION_REQUEST']._serialized_end=5869
  _globals['_CALLFUNCTION_RESPONSE']._serialized_start=5871
  _globals['_CALLFUNCTION_RESPONSE']._serialized_end=5952
  _globals['_PROVIDER']._serialized_start=5994
  _globals['_PROVIDER']._serialized_end=7205
  _globals['_PROVISIONER']._serialized_start=7208
  _globals['_PROVISIONER']._serialized_end=7542
# @@protoc_insertion_point(module_scope)
