import typer
from ssg.site import Site

def main(source="content", dest="dist"):
    config = {
        "dest": dest,
        "source": source
    }

    site = Site(**config).build()

typer.run(main)