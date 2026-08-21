import PageHeader from "../components/common/PageHeader";
import ReviewTable from "../components/review/ReviewTable";

function ReviewQueue() {

  return (

    <>

      <PageHeader
        title="Review Queue"
        subtitle="AI Validation Workspace"
      />

      <ReviewTable />

    </>

  );

}

export default ReviewQueue;