# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 51.0.0


from . import AWSObject, PropsDictType
from .validators import boolean


class ReportDefinition(AWSObject):
    """
    `ReportDefinition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cur-reportdefinition.html>`__
    """

    resource_type = "AWS::CUR::ReportDefinition"

    props: PropsDictType = {
        "AdditionalArtifacts": ([str], False),
        "AdditionalSchemaElements": ([str], False),
        "BillingViewArn": (str, False),
        "Compression": (str, True),
        "Format": (str, True),
        "RefreshClosedReports": (boolean, True),
        "ReportName": (str, True),
        "ReportVersioning": (str, True),
        "S3Bucket": (str, True),
        "S3Prefix": (str, True),
        "S3Region": (str, True),
        "TimeUnit": (str, True),
    }
