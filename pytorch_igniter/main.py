from aws_sagemaker_remote.training.main import sagemaker_training_main
from .args import train_args


def igniter_main(main, training_args=None, **sagemaker_args):
    r"""
    Run a training script

    Parameters
    ----------
    main : function
        Main function. Must have one argument ``parser:argparse.Namespace``.
    training_args : dict
        Keyword arguments to :meth:`pytorch_igniter.args.train_args`.
    sagemaker_args : dict
        Keyword arguments to ``aws-sagemaker-remote.training.main.sagemaker_training_main``.
        See `aws_sagemaker_remote <https://aws-sagemaker-remote.readthedocs.io/en/latest/>`_.
    """
    argparse_callback_input = sagemaker_args.get('argparse_callback', None)
    if training_args is None:
        training_args = {}

    def argparse_callback(parser):
        train_args(parser=parser, **training_args)
        if argparse_callback_input:
            argparse_callback_input(parser)
    sagemaker_args['argparse_callback'] = argparse_callback
    return sagemaker_training_main(
        main=main,
        **sagemaker_args
    )
