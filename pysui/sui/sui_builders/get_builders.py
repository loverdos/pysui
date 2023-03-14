#    Copyright Frank V. Castellucci
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#        http://www.apache.org/licenses/LICENSE-2.0
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

# -*- coding: utf-8 -*-
# pylint: disable=line-too-long

"""Sui Builders: Simple sui_getXXX calls."""

from typing import Final, Optional
from pysui.sui.sui_builders.base_builder import _NativeTransactionBuilder, sui_builder
from pysui.sui.sui_types.scalars import SuiNullType, SuiString, SuiInteger, ObjectID, SuiBoolean
from pysui.sui.sui_types.collections import SuiArray, SuiMap, EventID
from pysui.sui.sui_types.address import SuiAddress
from pysui.sui.sui_txresults.single_tx import (
    DelegatedStakes,
    DynamicFields,
    SuiCoinBalance,
    SuiCoinMetadata,
    CoinBalances,
    SuiCoinObjects,
    SuiLatestSystemState,
    ObjectInfo,
    ObjectRead,
    CommitteeInfo,
)
from pysui.sui.sui_txresults.complex_tx import (
    Checkpoint,
    CheckpointContents,
    CheckpointSummary,
    EventBlock,
    EventQueryEnvelope,
    TransactionQueryEnvelope,
    TxResponse,
    TxResponseArray,
)
from pysui.sui.sui_txresults.package_meta import (
    SuiMovePackage,
    SuiMoveModule,
    SuiMoveFunction,
    SuiMoveStruct,
    SuiMoveFunctionArgumentTypes,
)
import pysui.sui.sui_utils as sutils


class GetCoinMetaData(_NativeTransactionBuilder):
    """GetCoinMetaData returns meta data for a specific `coin_type`."""

    @sui_builder()
    def __init__(self, *, coin_type: Optional[SuiString] = "0x2::sui::SUI") -> None:
        """__init__ Initialize builder.

        :param coin_type: The specific coin type string, defaults to "0x2::sui::SUI"
        :type coin_type: SuiString, optional
        """
        super().__init__("sui_getCoinMetadata", handler_cls=SuiCoinMetadata, handler_func="from_dict")


class GetAllCoinBalances(_NativeTransactionBuilder):
    """GetAllCoinBalances Returns the total coin balances, for all coin types, owned by the address owner.."""

    @sui_builder()
    def __init__(self, *, owner: SuiAddress):
        """__init__ Initializes builder with address to fetch coin balances for.

        :param owner: the owner's Sui address
        :type owner: SuiAddress
        """
        super().__init__("sui_getAllBalances", handler_cls=CoinBalances, handler_func="ingest_data")


class GetAllCoins(_NativeTransactionBuilder):
    """GetAllCoins Returns all Coin objects owned by an address."""

    @sui_builder()
    def __init__(
        self,
        *,
        owner: SuiAddress,
        cursor: Optional[ObjectID] = None,
        limit: Optional[SuiInteger] = None,
    ):
        """__init__ Initialize builder.

        :param owner: the coin owner's address
        :type owner: SuiAddress
        :param cursor: Optional ObjectID as the starting item in returned page, defaults to None
        :type cursor: ObjectID, optional
        :param limit: Optional SuiInteger maximum number of items per page, defaults to None
        :type limit: SuiInteger, optional
        """
        super().__init__("sui_getAllCoins", handler_cls=SuiCoinObjects, handler_func="from_dict")


class GetCoinTypeBalance(_NativeTransactionBuilder):
    """GetCoinTypeBalance Return the total coin balance for a coin type."""

    @sui_builder()
    def __init__(self, *, owner: SuiAddress, coin_type: Optional[SuiString] = "0x2::sui::SUI"):
        """__init__ Initialize builder.

        :param owner: The owner's Sui address
        :type owner: SuiAddress
        :param coin_type: The specific coin type string, defaults to "0x2::sui::SUI"
        :type coin_type: SuiString, optional
        """
        super().__init__("sui_getBalance", handler_cls=SuiCoinBalance, handler_func="from_dict")


class GetCoins(_NativeTransactionBuilder):
    """Return the list of Coin objects of specific coin_type owned by an address."""

    @sui_builder()
    def __init__(
        self,
        *,
        owner: SuiAddress,
        coin_type: Optional[SuiString] = "0x2::sui::SUI",
        cursor: Optional[ObjectID] = None,
        limit: Optional[SuiInteger] = None,
    ):
        """__init__ Initialize builder.

        :param owner: the coin owner's Sui address
        :type owner: SuiAddress
        :param coin_type: fully qualified type names for the coin, defaults to "0x2::sui::SUI"
        :type coin_type: SuiString, optional
        :param cursor: Optional ObjectID as the starting item in returned page, defaults to None
        :type cursor: ObjectID, optional
        :param limit: maximum number of items per page, defaults to None
        :type limit: SuiInteger, optional
        """
        super().__init__("sui_getCoins", handler_cls=SuiCoinObjects, handler_func="from_dict")


class GetLatestSuiSystemState(_NativeTransactionBuilder):
    """GetLatestSuiSystemState return the latest known SUI system state."""

    @sui_builder()
    def __init__(self) -> None:
        """__init__ Initializes builder."""
        super().__init__("sui_getLatestSuiSystemState", handler_cls=SuiLatestSystemState, handler_func="from_dict")


class GetTotalSupply(_NativeTransactionBuilder):
    """Return the total supply for a given coin type (eg. 0x2::sui::SUI)."""

    @sui_builder()
    def __init__(
        self,
        *,
        coin_type: Optional[SuiString] = "0x2::sui::SUI",
    ) -> None:
        """__init__ Initialize builder.

        :param coin_type: fully qualified type names for the coin, defaults to "0x2::sui::SUI"
        :type coin_type: SuiString, optional
        """
        super().__init__("sui_getTotalSupply")


class GetObjectsOwnedByAddress(_NativeTransactionBuilder):
    """GetObjectsOwnedByAddress When executed, returns the list of objects owned by an address."""

    @sui_builder()
    def __init__(self, address: SuiAddress) -> None:
        """__init__ Initialize builder.

        :param address: The owner address to fetch list of ObjectInfo results
        :type address: SuiAddress
        """
        super().__init__("sui_getObjectsOwnedByAddress", handler_cls=ObjectInfo, handler_func="factory")


class GetDynamicFieldObject(_NativeTransactionBuilder):
    """GetDynamicFieldObject when executed, return the dynamic field object information for a specified object."""

    @sui_builder()
    def __init__(self, parent_object_id: ObjectID, name: SuiMap) -> None:
        """__init__ Builder initializer.

        :param parent_object_id: The ID of the queried parent object
        :type parent_object_id: ObjectID
        :param name: The Name of the dynamic field
        :type field_name: SuiString
        """
        super().__init__("sui_getDynamicFieldObject", handler_cls=ObjectRead, handler_func="factory")


class GetDynamicFields(_NativeTransactionBuilder):
    """GetDynamicFields when executed, returns the list of dynamic field objects owned by an object."""

    @sui_builder()
    def __init__(
        self, parent_object_id: ObjectID, cursor: Optional[ObjectID] = None, limit: Optional[SuiInteger] = None
    ) -> None:
        """__init__ Builder initializer.

        :param parent_object_id: The ID of the queried parent object
        :type parent_object_id: ObjectID
        :param cursor: Optional paging cursor, defaults to None
        :type cursor: ObjectID, optional
        :param limit: Maximum item returned per page, default to [QUERY_MAX_RESULT_LIMIT] if not specified, defaults to None
        :type cursor: SuiInteger, optional
        """
        super().__init__("sui_getDynamicFields", handler_cls=DynamicFields, handler_func="from_dict")


class GetObject(_NativeTransactionBuilder):
    """GetObject When executed, returns the object detailed information for a specified object."""

    _DEFAULT_GET_OBJECT_OPTIONS: Final[dict] = {
        "showType": True,
        "showOwner": True,
        "showPreviousTransaction": True,
        "showDisplay": True,
        "showContent": True,
        "showBcs": True,
        "showStorageRebate": True,
    }

    _DEFAULT_GET_PACKAGE_OPTIONS: Final[dict] = {
        "showType": True,
        "showOwner": True,
        "showPreviousTransaction": True,
        "showDisplay": False,
        "showContent": False,
        "showBcs": True,
        "showStorageRebate": True,
    }

    @sui_builder()
    def __init__(self, *, object_id: ObjectID, options: Optional[SuiMap] = None) -> None:
        """__init__ Initializes builder.

        :param object_id: Object identifier to fetch from chain
        :type object_id: ObjectID
        """
        super().__init__("sui_getObject", handler_cls=ObjectRead, handler_func="factory")
        if options is None or isinstance(options, SuiNullType):
            self.options = sutils.as_sui_map(self._DEFAULT_GET_OBJECT_OPTIONS.copy())
        else:
            self.options = sutils.as_sui_map(options)

    @classmethod
    def object_options(cls) -> dict:
        """object_options get the default options for sui_getObject.

        :return: The default options map
        :rtype: dict
        """
        return cls._DEFAULT_GET_OBJECT_OPTIONS.copy()

    @classmethod
    def package_options(cls) -> dict:
        """package_options get the options that correctly fetch package objects.

        :return: The package options map
        :rtype: dict
        """
        return cls._DEFAULT_GET_PACKAGE_OPTIONS.copy()


class GetMultipleObjects(_NativeTransactionBuilder):
    """GetMultipleObjects When executed, returns the objects detailed information for a list of object identifiers."""

    @sui_builder()
    def __init__(self, *, object_ids: SuiArray[ObjectID], options: Optional[SuiMap] = None) -> None:
        """__init__ Initializes builder.

        :param object_ids: SuiArray[ObjectID] of object identifiers to fetch from chain
        :type object_ids: SuiArray
        """
        super().__init__("sui_multiGetObjects", handler_cls=ObjectRead, handler_func="factory")
        if options is None or isinstance(options, SuiNullType):
            self.options = sutils.as_sui_map(GetObject._DEFAULT_GET_OBJECT_OPTIONS.copy())
        else:
            self.options = sutils.as_sui_map(options)

    @classmethod
    def object_options(cls) -> dict:
        """object_options get the default options for sui_getObject.

        :return: The default options map
        :rtype: dict
        """
        return GetObject.object_options()

    @classmethod
    def package_options(cls) -> dict:
        """package_options get the options that correctly fetch package objects.

        :return: The package options map
        :rtype: dict
        """
        return GetObject.package_options()


class GetPastObject(_NativeTransactionBuilder):
    """GetPastObject When executed, return the object information for a specified version.

    Note there is no software-level guarantee/SLA that objects with past versions can be retrieved by this API,
    even if the object and version exists/existed. The result may vary across nodes depending on their pruning
    policies.
    """

    @sui_builder()
    def __init__(self, object_id: ObjectID, version: SuiInteger, options: Optional[SuiMap] = None) -> None:
        """__init__ Initialize builder.

        :param sui_object: Object identifier to fetch from chain, defaults to None
        :type sui_object: ObjectID, optional
        :param version: Specific version sequence number being requested, defaults to None
        :type version: SuiInteger, optional
        """
        super().__init__("sui_tryGetPastObject", handler_cls=ObjectRead, handler_func="factory")
        if options is None or isinstance(options, SuiNullType):
            self.options = sutils.as_sui_map(GetObject._DEFAULT_GET_OBJECT_OPTIONS.copy())
        else:
            self.options = sutils.as_sui_map(options)


class GetMultiplePastObjects(_NativeTransactionBuilder):
    """GetMultiplePastObjects When executed, return the object information for a specified version.

    Note there is no software-level guarantee/SLA that objects with past versions can be retrieved by this API,
    even if the object and version exists/existed. The result may vary across nodes depending on their pruning
    policies.
    """

    @sui_builder()
    def __init__(self, past_objects: SuiArray[SuiMap], options: Optional[SuiMap] = None) -> None:
        """__init__ Initialize builder.

        :param sui_object: Object identifier to fetch from chain, defaults to None
        :type sui_object: ObjectID, optional
        :param version: Specific version sequence number being requested, defaults to None
        :type version: SuiInteger, optional
        """
        super().__init__("sui_tryMultiGetPastObjects", handler_cls=ObjectRead, handler_func="factory")
        if options is None or isinstance(options, SuiNullType):
            self.options = sutils.as_sui_map(GetObject._DEFAULT_GET_OBJECT_OPTIONS.copy())
        else:
            self.options = sutils.as_sui_map(options)


class GetPackage(_NativeTransactionBuilder):
    """GetPackage When executed, return structured representations of all modules in the given package."""

    @sui_builder()
    def __init__(self, *, package: ObjectID) -> None:
        """__init__ Initialize GetPackage object.

        :param package: ObjectID of package to query, defaults to None
        :type package: ObjectID, optional
        """
        super().__init__(
            "sui_getNormalizedMoveModulesByPackage", handler_cls=SuiMovePackage, handler_func="ingest_data"
        )


class GetModule(_NativeTransactionBuilder):
    """GetModule When executed, returns the structural representation of a module.

    Includes general Module informationn as well as structure and function definitions.
    """

    @sui_builder()
    def __init__(self, *, package: ObjectID, module_name: SuiString) -> None:
        """__init__ Initialize GetModule object.

        :param package: ObjectID of package to query
        :type package: ObjectID
        :param module_name: Name of module from package to fetch
        :type module_name: SuiString
        """
        super().__init__("sui_getNormalizedMoveModule", handler_cls=SuiMoveModule, handler_func="ingest_data")


class GetFunction(_NativeTransactionBuilder):
    """GetFunction When executed, returns the structural representation of a module's function.

    Includes general function arguments and return type definitions.
    """

    @sui_builder()
    def __init__(self, *, package: ObjectID, module_name: SuiString, function_name: SuiString) -> None:
        """__init__ Initialize GetModule object.

        :param package: ObjectID of package to query
        :type package: ObjectID
        :param module_name: Name of module from package containing function_name to fetch
        :type module_name: SuiString
        :param function_name: Name of module from package to fetch
        :type function_name: SuiString
        """
        super().__init__("sui_getNormalizedMoveFunction", handler_cls=SuiMoveFunction, handler_func="ingest_data")


class GetFunctionArgs(_NativeTransactionBuilder):
    """GetFunction When executed, returns the argument types of a Move function."""

    @sui_builder()
    def __init__(self, *, package: ObjectID, module: SuiString, function: SuiString) -> None:
        """__init__ Initialize GetModule object.

        :param package: ObjectID of package to query
        :type package: ObjectID
        :param module: Name of module from package containing function_name to fetch
        :type module: SuiString
        :param function: Name of module's function to fetch arguments for
        :type function: SuiString
        """
        super().__init__(
            "sui_getMoveFunctionArgTypes", handler_cls=SuiMoveFunctionArgumentTypes, handler_func="ingest_data"
        )


class GetStructure(_NativeTransactionBuilder):
    """GetStructure When executed, returns a module's structure representation."""

    @sui_builder()
    def __init__(self, *, package: ObjectID, module_name: SuiString, structure_name: SuiString) -> None:
        """__init__ Initialize GetModule object.

        :param package: ObjectID of package to query
        :type package: ObjectID
        :param module_name: Name of module from package containing function_name to fetch
        :type module_name: SuiString
        :param structure_name: Name of structure from structure to fetch
        :type structure_name: SuiString
        """
        super().__init__("sui_getNormalizedMoveStruct", handler_cls=SuiMoveStruct, handler_func="ingest_data")


class GetRpcAPI(_NativeTransactionBuilder):
    """GetRpcAPI When executed, returns full list of SUI node RPC API supported."""

    @sui_builder()
    def __init__(self) -> None:
        """Initialize builder."""
        super().__init__("rpc.discover")


class GetCommittee(_NativeTransactionBuilder):
    """GetCommittee When executed, returns information on committee (collection of nodes)."""

    @sui_builder()
    def __init__(self, epoch: Optional[SuiInteger] = None) -> None:
        """__init__ GetCommitttee Builder initializer.

        :param epoch: Epoch to return state of committee from, defaults to None
        :type epoch: SuiInteger, optional
        """
        super().__init__("sui_getCommitteeInfo", handler_cls=CommitteeInfo, handler_func="factory")


# Event Query Types


class SenderEventQuery(SuiMap):
    """Query events for Sender address."""

    def __init__(self, sender: SuiAddress):
        """Initialize query parameter."""
        super().__init__("Sender", sender.value.value)


class TransactionEventQuery(SuiMap):
    """Query events for Transaction."""

    def __init__(self, txid: str):
        """Initialize query parameter."""
        super().__init__("Transaction", txid)


class PackageEventQuery(SuiMap):
    """Query events for Transaction."""

    def __init__(self, txid: str):
        """Initialize query parameter."""
        super().__init__("Package", txid)


class MoveModuleEventQuery(SuiMap):
    """Query events for Move Module."""

    def __init__(self, module: str, package: str) -> None:
        """Initialize query parameter."""
        sdict = {"module": module, "package": package}
        super().__init__("MoveModule", sdict)


class MoveEventTypeQuery(SuiMap):
    """Query events for Move Event on Struct type."""

    def __init__(self, struct: str):
        """Initialize query parameter."""
        super().__init__("MoveEventType", struct)


class MoveEventField(SuiMap):
    """Query events for Move Event fields."""

    def __init__(self, field_path: dict[str, str]):
        """Initialize query parameter.

        field_path argument is dict with {'path':PATH_TO_FILE,'value':true}
        """
        super().__init__("MoveEventField", field_path)


# TODO: Deprecated
# class EventTypeQuery(SuiMap):
#     """Query events for Event types."""

#     _evtype_set = {
#         "MoveEvent",
#         "Publish",
#         "CoinBalanceChange",
#         "EpochChange",
#         "Checkpoint",
#         "TransferObject",
#         "MutateObject",
#         "DeleteObject",
#         "NewObject",
#     }

#     def __init__(self, event_type: str):
#         """Initialize query parameter."""
#         if event_type in self._evtype_set:
#             super().__init__("EventType", event_type)
#         else:
#             raise ValueError(f"event_type: {event_type} not one of {self._evtype_set}")

# TODO: Deprecated
# class RecipientEventQuery(SuiMap):
#     """Query events for Recipient address."""

#     def __init__(self, recipient: SuiAddress):
#         """Initialize query parameter."""
#         sdict = {"AddressOwner": recipient.value.value}
#         super().__init__("Recipient", sdict)


# TODO: Deprecated
# class ObjectEventQuery(SuiMap):
#     """Query events for Object id."""

#     def __init__(self, object_id: ObjectID):
#         """Initialize query parameter."""
#         super().__init__("Object", object_id.value)


class TimeRangeEventQuery(SuiMap):
    """Query events for Time Range."""

    def __init__(self, start_time: SuiInteger, end_time: SuiInteger):
        """Initialize query parameter."""
        sdict = {"startTime": start_time.value, "endTime": end_time.value}
        super().__init__("TimeRange", sdict)


# TODO: Implement All, Any, And and Or constructs
class QueryEvents(_NativeTransactionBuilder):
    """QueryEvents takes event query criteria (options) as parameters and returns events matching criteria."""

    @sui_builder()
    def __init__(
        self,
        *,
        query: SuiMap,
        cursor: Optional[EventID] = None,
        limit: Optional[SuiInteger] = None,
        descending_order: Optional[SuiBoolean] = None,
    ) -> None:
        """Initialize builder."""
        super().__init__("sui_queryEvents", handler_cls=EventQueryEnvelope, handler_func="from_dict")


class GetEvents(_NativeTransactionBuilder):
    """GetEvents When executed, return list of events for a specified query criteria."""

    @sui_builder()
    def __init__(
        self,
        *,
        transaction_digest: SuiString,
    ) -> None:
        """Initialize builder."""
        super().__init__("sui_getEvents", handler_cls=EventBlock, handler_func="factory")
        # super().__init__("sui_getEvents", handler_cls=EventQueryEnvelope, handler_func="from_dict")


class GetTotalTxCount(_NativeTransactionBuilder):
    """GetTotalTxCount When executed, return the total number of transactions known to the server."""

    @sui_builder()
    def __init__(self) -> None:
        """Initialize builder."""
        super().__init__("sui_getTotalTransactionNumber")


class GetTx(_NativeTransactionBuilder):
    """GetTx When executed, return the transaction response object."""

    _DEFAULT_GET_TX_OPTIONS: Final[dict] = {
        "showEffects": True,
        "showEvents": True,
        "showInput": False,
    }

    @sui_builder()
    def __init__(self, *, digest: SuiString, options: Optional[SuiMap] = None) -> None:
        """Initialize builder."""
        super().__init__("sui_getTransaction", handler_cls=TxResponse, handler_func="from_dict")
        if options is None or isinstance(options, SuiNullType):
            self.options = sutils.as_sui_map(self._DEFAULT_GET_TX_OPTIONS.copy())
        else:
            self.options = sutils.as_sui_map(options)

    @classmethod
    def default_options(cls) -> dict:
        """default_options get the default options for fetching transactions.

        :return: The option flags map for `sui_getTransaction`
        :rtype: dict
        """
        return cls._DEFAULT_GET_TX_OPTIONS.copy()


class GetMultipleTx(_NativeTransactionBuilder):
    """."""

    @sui_builder()
    def __init__(self, *, digests: SuiArray, options: Optional[SuiMap] = None) -> None:
        """Initialize builder."""
        super().__init__("sui_multiGetTransactions", handler_cls=TxResponseArray, handler_func="factory")
        if options is None or isinstance(options, SuiNullType):
            self.options = sutils.as_sui_map(GetTx._DEFAULT_GET_TX_OPTIONS.copy())
        else:
            self.options = sutils.as_sui_map(options)

    @classmethod
    def default_options(cls) -> dict:
        """default_options get the default options for fetching transactions.

        :return: The option flags map for `sui_multiGetTransactions`
        :rtype: dict
        """
        return GetTx.default_options()


class GetTxsMoveFunction(SuiMap):
    """For GetTxns."""

    def __init__(self, package: str, function: str, module: str):
        """Initialize query params."""
        super().__init__("MoveFunction", {"package": package, "function": function, "module": module})


class GetTxsInputObject(SuiMap):
    """For GetTxns."""

    def __init__(self, object_id: str):
        """Initialize query params."""
        super().__init__("InputObject", object_id)


class GetTxsMutateObject(SuiMap):
    """For GetTxns."""

    def __init__(self, object_id: str):
        """Initialize query params."""
        super().__init__("MutatedObject", object_id)


class GetTxsFromAddress(SuiMap):
    """For GetTxns."""

    def __init__(self, address_id: str):
        """Initialize query params."""
        super().__init__("FromAddress", address_id)


class GetTxsToAddress(SuiMap):
    """For GetTxns."""

    def __init__(self, address_id: str):
        """Initialize query params."""
        super().__init__("ToAddress", address_id)


class GetTxs(_NativeTransactionBuilder):
    """Return information about a specific transaction."""

    @sui_builder()
    def __init__(
        self,
        *,
        query: SuiMap,
        cursor: Optional[SuiString] = None,
        limit: Optional[SuiInteger] = None,
        descending_order: Optional[SuiBoolean] = None,
    ) -> None:
        """Initialize builder."""
        super().__init__("sui_queryTransactions", handler_cls=TransactionQueryEnvelope, handler_func="from_dict")


class GetTransactionsInRange(_NativeTransactionBuilder):
    """Return list of transaction digests within the queried range."""

    @sui_builder()
    def __init__(
        self,
        *,
        start: SuiInteger,
        end: SuiInteger,
    ) -> None:
        """Initialize builder."""
        super().__init__("sui_getTransactionsInRangeDeprecated")


class GetDelegatedStakes(_NativeTransactionBuilder):
    """GetDelegatedStakes return all [DelegatedStake] coins for address owner."""

    @sui_builder()
    def __init__(self, owner: SuiAddress):
        """__init__ Builder initializer.

        :param owner: SuiAddress of staked coin owner
        :type owner: SuiAddress
        """
        super().__init__("sui_getDelegatedStakes", handler_cls=DelegatedStakes, handler_func="ingest_data")


class GetCheckpointContentsByDigest(_NativeTransactionBuilder):
    """GetCheckpointContentsByDigest return contents of a checkpoint based on its sequence number."""

    @sui_builder()
    def __init__(self, digest: SuiString):
        """__init__ Builder initializer.

        :param digest: Checkpint content digest
        :type digest: SuiString
        """
        super().__init__("sui_getCheckpointContentsByDigest", handler_cls=CheckpointContents, handler_func="from_dict")


class GetCheckpointSummary(_NativeTransactionBuilder):
    """GetCheckpointSummary return a checkpoint summary based on a checkpoint sequence number."""

    @sui_builder()
    def __init__(self, sequence_number: SuiInteger):
        """__init__ Builder initializer.

        :param sequence_number: Sequence number to get checkpoint contents summary for
        :type sequence_number: SuiInteger
        """
        super().__init__("sui_getCheckpointSummary", handler_cls=CheckpointSummary, handler_func="from_dict")


class GetCheckpointSummaryByDigest(_NativeTransactionBuilder):
    """GetCheckpointSummaryByDigest return a checkpoint summary based on checkpoint digest."""

    @sui_builder()
    def __init__(self, digest: SuiString):
        """__init__ Builder initializer.

        :param digest: Checkpint content digest
        :type digest: SuiString
        """
        super().__init__("sui_getCheckpointSummaryByDigest", handler_cls=CheckpointSummary, handler_func="from_dict")


class GetLatestCheckpointSequence(_NativeTransactionBuilder):
    """GetLatestCheckpointSequence return the sequence number of the latest checkpoint that has been executed."""

    @sui_builder()
    def __init__(self):
        """__init__ Builder initializer."""
        super().__init__("sui_getLatestCheckpointSequenceNumber")


class GetCheckpointByDigest(_NativeTransactionBuilder):
    """GetCheckpointByDigest return a checkpoint for cp_id."""

    @sui_builder()
    def __init__(self, cp_id: SuiString):
        """__init__ Builder initializer.

        :param cp_id: Checkpoint digest id
        :type cp_id: SuiString
        """
        super().__init__("sui_getCheckpoint", handler_cls=Checkpoint, handler_func="from_dict")


class GetCheckpointBySequence(_NativeTransactionBuilder):
    """GetCheckpoint return a checkpoint for cp_id."""

    @sui_builder()
    def __init__(self, cp_seq: SuiInteger):
        """__init__ Builder initializer.

        :param cp_id: Checkpoint sequence number
        :type cp_id: SuiString
        """
        super().__init__("sui_getCheckpoint", handler_cls=Checkpoint, handler_func="from_dict")


class GetReferenceGasPrice(_NativeTransactionBuilder):
    """GetReferenceGasPrice return the reference gas price for the network."""

    @sui_builder()
    def __init__(self):
        """Builder initializer."""
        super().__init__("sui_getReferenceGasPrice")
