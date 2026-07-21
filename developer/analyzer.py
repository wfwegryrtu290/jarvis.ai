def analyze(report):

    summary = []

    if report["success"]:
        summary.append("Няма синтактични грешки.")

    for error in report["errors"]:

        summary.append(
            f"{error['file']} -> {error['error']}"
        )

    return "\n".join(summary)