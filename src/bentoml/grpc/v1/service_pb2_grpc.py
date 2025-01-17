# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from bentoml.grpc.v1 import service_pb2 as bentoml_dot_grpc_dot_v1_dot_service__pb2


class BentoServiceStub(object):
    """a gRPC BentoServer.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Call = channel.unary_unary(
                '/bentoml.grpc.v1.BentoService/Call',
                request_serializer=bentoml_dot_grpc_dot_v1_dot_service__pb2.Request.SerializeToString,
                response_deserializer=bentoml_dot_grpc_dot_v1_dot_service__pb2.Response.FromString,
                )


class BentoServiceServicer(object):
    """a gRPC BentoServer.
    """

    def Call(self, request, context):
        """Call handles methodcaller of given API entrypoint.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BentoServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Call': grpc.unary_unary_rpc_method_handler(
                    servicer.Call,
                    request_deserializer=bentoml_dot_grpc_dot_v1_dot_service__pb2.Request.FromString,
                    response_serializer=bentoml_dot_grpc_dot_v1_dot_service__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'bentoml.grpc.v1.BentoService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BentoService(object):
    """a gRPC BentoServer.
    """

    @staticmethod
    def Call(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bentoml.grpc.v1.BentoService/Call',
            bentoml_dot_grpc_dot_v1_dot_service__pb2.Request.SerializeToString,
            bentoml_dot_grpc_dot_v1_dot_service__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
